import pandas as pd
import os
import numpy as np

student_data = pd.read_csv("student.csv")

average_cgpa = student_data["CGPA"].mean()
print("Average CGPA of students:", average_cgpa)

high_cgpa_students = student_data[student_data["CGPA"] > 9]
print("\nStudents with CGPA > 9:\n", high_cgpa_students)

cse_high_cgpa_students = student_data[(student_data["Branch"] == "CSE") & (student_data["CGPA"] > 9)]
print("\nCSE Students with CGPA > 9:\n", cse_high_cgpa_students)

max_cgpa_student = student_data.loc[student_data["CGPA"].idxmax()]
print("\nStudent with Maximum CGPA:\n", max_cgpa_student)

branch_avg_cgpa = student_data.groupby("Branch")["CGPA"].mean()
print("\nAverage CGPA of each branch:\n", branch_avg_cgpa)