'''Question 6
Consider the following tables.
Student
| StudentID | Name | CourseID |
| --------- | ----- | -------- |
| 1 | Rahul | 201 |
| 2 | Neha | 202 |
| 3 | Aman | NULL |
Course
| CourseID | CourseName |
| -------- | ---------- |
| 201 | Python |
| 202 | SQL |
Write an SQL query to display all students along with their course names
using a LEFT JOIN.
'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE Student (
        StudentID INT,
        Name VARCHAR(50),
        CourseID INT
    )
""")

cursor.execute("""
    CREATE TABLE Course (
        CourseID INT,
        CourseName VARCHAR(50)
    )
""")

# Aman has NULL CourseID, so he is not enrolled in any course
students = [
    (1, "Rahul", 201),
    (2, "Neha", 202),
    (3, "Aman", None)
]
cursor.executemany("INSERT INTO Student VALUES (?, ?, ?)", students)

courses = [
    (201, "Python"),
    (202, "SQL")
]
cursor.executemany("INSERT INTO Course VALUES (?, ?)", courses)

# LEFT JOIN keeps all students, even if they don't have a matching course
print("Students with their course names (LEFT JOIN):")
cursor.execute("""
    SELECT Student.Name, Course.CourseName
    FROM Student
    LEFT JOIN Course
    ON Student.CourseID = Course.CourseID
""")
for row in cursor.fetchall():
    print(row)

connection.close()