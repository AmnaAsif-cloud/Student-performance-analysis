import pandas as pd
import matplotlib.pyplot as plt
import os


# Create folder for charts
os.makedirs("charts", exist_ok=True)


# ==========================
# Load Dataset
# ==========================

data = pd.read_csv("student_data.csv")


print("\nFirst 5 Rows:")
print(data.head())


# ==========================
# Dataset Information
# ==========================

print("\nDataset Information:")
data.info()


print("\nStatistical Summary:")
print(data.describe())


# ==========================
# Average Final Score
# ==========================

average_score = data["Final_Score"].mean()

print(
    "\nAverage Final Score:",
    round(average_score, 2)
)


# ==========================
# Highest Scoring Student
# ==========================

top_student = data.loc[
    data["Final_Score"].idxmax()
]


print(
    "Top Student:",
    top_student["Name"]
)

print(
    "Highest Score:",
    top_student["Final_Score"]
)


# ==========================
# Study Hours vs Final Score
# ==========================

plt.figure(figsize=(7,5))


plt.scatter(
    data["Study_Hours"],
    data["Final_Score"]
)


plt.xlabel(
    "Study Hours"
)

plt.ylabel(
    "Final Score"
)


plt.title(
    "Study Hours vs Final Score"
)


plt.grid(True)


plt.tight_layout()


plt.savefig(
    "charts/study_hours_vs_score.png"
)


plt.show()



# ==========================
# Student Attendance Analysis
# ==========================

plt.figure(figsize=(10,5))


plt.bar(
    data["Name"],
    data["Attendance"]
)


plt.xlabel(
    "Students"
)


plt.ylabel(
    "Attendance Percentage"
)


plt.title(
    "Student Attendance"
)


plt.xticks(
    rotation=45
)


plt.tight_layout()


plt.savefig(
    "charts/student_attendance.png"
)


plt.show()



# ==========================
# Final Score Distribution
# ==========================

plt.figure(figsize=(7,5))


plt.hist(
    data["Final_Score"],
    bins=10
)


plt.xlabel(
    "Final Score"
)


plt.ylabel(
    "Number of Students"
)


plt.title(
    "Final Score Distribution"
)


plt.tight_layout()


plt.savefig(
    "charts/score_distribution.png"
)


plt.show()



# ==========================
# Study Hours Average
# ==========================

average_hours = data["Study_Hours"].mean()


print(
    "\nAverage Study Hours:",
    round(average_hours,2)
)



# ==========================
# Attendance Average
# ==========================

average_attendance = data["Attendance"].mean()


print(
    "Average Attendance:",
    round(average_attendance,2)
)



# ==========================
# Correlation Analysis
# ==========================

correlation = data[
    "Study_Hours"
].corr(
    data["Final_Score"]
)


print(
    "\nStudy Hours and Final Score Correlation:",
    round(correlation,2)
)


if correlation > 0:
    print(
        "Insight: Students with more study hours tend to have higher scores."
    )

else:
    print(
        "Insight: Study hours do not show a positive relationship with scores."
    )