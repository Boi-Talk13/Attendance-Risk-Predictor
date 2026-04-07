#  AI-Powered Attendance Risk Analyzer

##  Overview
This project is an **Agentic AI system** that analyzes student attendance and identifies academic risk levels using **LangChain, Groq (LLM), and custom tools**.

It combines:
- Rule-based logic (attendance policies)
- AI reasoning (LLM)
- Structured reporting

---

##  Tech Stack
- **Backend**: Python
- **AI Model**: Groq (LLaMA 3.1)
- **Framework**: LangChain + LangGraph
- **Data Handling**: Pandas
- **Dataset**: CSV (student_attendance.csv)

---

## 🚀 Features
- Student attendance risk analysis  
- Rule-based compliance checking (75% policy)  
- Trend analysis (last 5 days)  
- AI-generated academic insights  
- Structured professional report output  

---

## 📂 Project Structure
```
├── test3.py                  # Main program
├── student_attendance.csv    # Dataset
├── README.md                 # Documentation
```

---

##  How It Works

### Step 1: Input
User enters a **Student ID**

### Step 2: Data Fetch
Program reads student details from CSV:
- Name  
- Attendance %  
- Recent trend  

### Step 3: AI Agent Processing
- LLM receives query  
- Calls tools:  
  - calculate_risk_threshold()  
  - evaluate_absence_trend()  

### Step 4: Report Generation
AI generates structured output:

```
╔════════════════════════════════════════════════════╗
║       UNIVERSITY ATTENDANCE ANALYTICS REPORT       ║
╠════════════════════════════════════════════════════╣
  STUDENT    : Student_0
  COMPLIANCE : CRITICAL: 65.65%
  BEHAVIOR   : NEGATIVE: 5/5 days absent
  SYNOPSIS   : High academic risk detected
  STRATEGY   : Intensive Support (...)
╚════════════════════════════════════════════════════╝
```

---

##  Custom Tools

### 1. Attendance Risk Tool
```
calculate_risk_threshold(percentage)
```
- < 75 → CRITICAL  
- 75–80 → BORDERLINE  
- > 80 → STABLE  

### 2. Trend Analysis Tool
```
evaluate_absence_trend(history)
```
- Counts 'A' (absent days)  
- ≥ 3 → NEGATIVE  
- < 3 → CONSISTENT  

---

## 🤖 Agent Architecture
- ReAct Agent (Reason + Act)

Flow:
1. Understand query  
2. Decide which tool to use  
3. Execute tool  
4. Generate final response  

---

## ▶️ How to Run

### 1. Install Dependencies
```
pip install pandas langchain langchain-groq langgraph
```

### 2. Set API Key
```
export GROQ_API_KEY="your_api_key"
```

### 3. Run the Program
```
python test3.py
```

### 4. Enter Student ID
```
PROMPT: Enter Student ID (101-200):
```

---

## ⚠️ Limitations
- No input validation  
- Hardcoded API key (not secure)  
- Simple rule-based logic (no ML prediction)  
- CLI-based (no UI)  

---



## 🧾 One-Line Summary
This project uses an AI agent to analyze student attendance by combining rule-based tools with LLM reasoning and generates structured academic risk reports.

---

