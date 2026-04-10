import pandas as pd
import random

# Create synthetic data
data = {
    "Student_ID": [101 + i for i in range(100)],
    "Name": [f"Student_{i}" for i in range(100)],
    "Attendance_Percentage": [round(random.uniform(50, 98), 2) for _ in range(100)],
    "Recent_Trend": [random.choice(["P,P,P,P,P", "P,A,P,A,A", "A,A,A,A,A", "P,P,A,A,A"]) for _ in range(100)]
}

df = pd.DataFrame(data)
df.to_csv("student_attendance.csv", index=False)
print("Dataset 'student_attendance.csv' has been created successfully!")