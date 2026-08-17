import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Create Student Data
# --------------------------------------------------

data = {
    "Student": [
        "Anu", "Ravi", "Priya", "Kiran", "Sneha",
        "Arjun", "Meena", "Rahul", "Divya", "Vijay"
    ],

    "Math": [85, 65, 92, 55, 78, 88, 72, 60, 95, 70],

    "Science": [78, 70, 88, 60, 82, 90, 75, 65, 91, 73],

    "English": [90, 68, 95, 62, 85, 87, 80, 70, 94, 76],

    "Attendance": [92, 75, 96, 68, 88, 94, 82, 72, 98, 79]
}

df = pd.DataFrame(data)


# --------------------------------------------------
# 2. Display Student Data
# --------------------------------------------------

print("\n===== STUDENT DATA =====")
print(df)


# --------------------------------------------------
# 3. Check for Missing Values
# --------------------------------------------------

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# --------------------------------------------------
# 4. Calculate Total Marks
# --------------------------------------------------

df["Total"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
)


# --------------------------------------------------
# 5. Calculate Average Marks
# --------------------------------------------------

df["Average"] = df["Total"] / 3


print("\n===== STUDENT PERFORMANCE =====")
print(df)


# --------------------------------------------------
# 6. Find Top Student
# --------------------------------------------------

top_student = df.loc[df["Average"].idxmax()]

print("\n===== TOP STUDENT =====")
print("Name:", top_student["Student"])
print("Average Marks:", round(top_student["Average"], 2))


# --------------------------------------------------
# 7. Find Lowest Performing Student
# --------------------------------------------------

lowest_student = df.loc[df["Average"].idxmin()]

print("\n===== LOWEST PERFORMING STUDENT =====")
print("Name:", lowest_student["Student"])
print("Average Marks:", round(lowest_student["Average"], 2))


# --------------------------------------------------
# 8. Calculate Subject Averages
# --------------------------------------------------

subject_averages = df[
    ["Math", "Science", "English"]
].mean()

print("\n===== SUBJECT AVERAGES =====")
print(subject_averages)


# --------------------------------------------------
# 9. Students With Good Attendance
# --------------------------------------------------

good_attendance = df[df["Attendance"] >= 80]

print("\n===== STUDENTS WITH GOOD ATTENDANCE =====")
print(
    good_attendance[
        ["Student", "Attendance"]
    ]
)


# --------------------------------------------------
# 10. Students Who Need Improvement
# --------------------------------------------------

students_needing_help = df[df["Average"] < 60]

print("\n===== STUDENTS NEEDING IMPROVEMENT =====")

if students_needing_help.empty:
    print("No students need improvement.")

else:
    print(
        students_needing_help[
            ["Student", "Average"]
        ]
    )


# --------------------------------------------------
# 11. Student Ranking
# --------------------------------------------------

ranking = df.sort_values(
    "Average",
    ascending=False
)

print("\n===== STUDENT RANKING =====")

print(
    ranking[
        ["Student", "Average"]
    ]
)


# --------------------------------------------------
# 12. Class Summary
# --------------------------------------------------

print("\n===== CLASS SUMMARY =====")

print("Total Students:", len(df))

print(
    "Class Average:",
    round(df["Average"].mean(), 2)
)

print(
    "Average Attendance:",
    round(df["Attendance"].mean(), 2),
    "%"
)


# --------------------------------------------------
# 13. Bar Chart - Student Performance
# --------------------------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    df["Student"],
    df["Average"]
)

plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.title(
    "Student Average Performance"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# --------------------------------------------------
# 14. Bar Chart - Subject Performance
# --------------------------------------------------

plt.figure(figsize=(7, 5))

plt.bar(
    subject_averages.index,
    subject_averages.values
)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.title(
    "Average Marks by Subject"
)

plt.tight_layout()

plt.show()


# --------------------------------------------------
# 15. Attendance vs Performance
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance"],
    df["Average"]
)

plt.xlabel("Attendance (%)")

plt.ylabel("Average Marks")

plt.title(
    "Attendance vs Student Performance"
)

plt.tight_layout()

plt.show()


print("\n===== ANALYSIS COMPLETED =====")