import os
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent 


os.environ["GROQ_API_KEY"] = "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"

@tool
def calculate_risk_threshold(percentage: float):
    """Checks the current attendance against the 75% university policy."""
    perc = float(percentage)
    if perc < 75:
        return f"CRITICAL: {perc}% (Below 75% Mandatory Limit)"
    if perc < 80:
        return f"BORDERLINE: {perc}% (Near 75% Threshold)"
    return f"STABLE: {perc}% (Above 80% Requirement)"

@tool
def evaluate_absence_trend(history: str):
    """Analyzes the 5-day attendance pattern."""
    absences = history.count('A')
    if absences >= 3:
        return f"NEGATIVE: {absences}/5 days absent (Recent Drop)"
    return f"CONSISTENT: {absences}/5 days absent (Regular)"

tools = [calculate_risk_threshold, evaluate_absence_trend]

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

system_instructions = (
    "You are a Senior Academic Risk Auditor. Maintain a formal and data-driven tone. "
    "Do not use emojis or conversational fillers. "
    "Use the following EXACT visual template. "
    "For the STRATEGY, if you use terms like 'Intensive Support' or 'Academic Probation', "
    "you MUST include a brief meaning in brackets so it is easy to understand.\n\n"
    "╔════════════════════════════════════════════════════╗\n"
    "║       UNIVERSITY ATTENDANCE ANALYTICS REPORT       ║\n"
    "╠════════════════════════════════════════════════════╣\n"
    "  STUDENT    : [Name]\n"
    "  COMPLIANCE : [Output from calculate_risk_threshold]\n"
    "  BEHAVIOR   : [Output from evaluate_absence_trend]\n"
    "  SYNOPSIS   : [1-sentence analytical insight linking perc & trend]\n"
    "  STRATEGY   : [Instruction] ([Brief Meaning])\n"
    "╚════════════════════════════════════════════════════╝"
)

# 5. Build the Agent
agent_executor = create_react_agent(llm, tools, prompt=system_instructions)

# 6. Implementation
def run_project():
    try:
        if not os.path.exists("student_attendance.csv"):
            print("[SYSTEM ERROR] student_attendance.csv not found.")
            return

        df = pd.read_csv("student_attendance.csv")
        
        print("\n" + "═"*54)
        print(" [SYSTEM] INITIALIZING ATTENDANCE RISK ENGINE... ")
        print("═"*54)
        
        s_id = int(input("\nPROMPT: Enter Student ID (101-200): "))
        student_data = df[df['Student_ID'] == s_id]
        
        if not student_data.empty:
            name = student_data.iloc[0]['Name']
            perc = student_data.iloc[0]['Attendance_Percentage']
            trend = student_data.iloc[0]['Recent_Trend']
            
            query = f"Audit Student {name}. Attendance: {perc}%, Trend: {trend}."
            print(f"\n[ANALYZING] Evaluating risk vectors for {name}...\n")
            
            result = agent_executor.invoke({"messages": [("human", query)]})
            
            # Print the final classy output
            print(result["messages"][-1].content + "\n")
        else:
            print(f"[INVALID] Student ID {s_id} not found in database.")

    except Exception as e:
        print(f"[FATAL ERROR] {e}")

if __name__ == "__main__":
    run_project()