'''Question 10
Consider the following tables.
Student
| StudentID | Name | CourseID |
| --------- | ----- | -------- |
| 1 | Rahul | 101 |
| 2 | Neha | 102 |
| 3 | Aman | 101 |
Course
| CourseID | CourseName |
| -------- | ---------- |
| 101 | Python |
| 102 | Java |
Write SQL queries to:
1. Display Student Name and Course Name using an INNER JOIN.
2. Display only students enrolled in the Python course using the WHERE
clause.
3. Create a view named 'PythonStudents' for students enrolled in the Python
course.'''

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

students = [
    (1, "Rahul", 101),
    (2, "Neha", 102),
    (3, "Aman", 101)
]
cursor.executemany("INSERT INTO Student VALUES (?, ?, ?)", students)

courses = [
    (101, "Python"),
    (102, "Java")
]
cursor.executemany("INSERT INTO Course VALUES (?, ?)", courses)

# 1. Student Name and Course Name using INNER JOIN
print("1. Student Name and Course Name (INNER JOIN):")
cursor.execute("""
    SELECT Student.Name, Course.CourseName
    FROM Student
    INNER JOIN Course
    ON Student.CourseID = Course.CourseID
""")
for row in cursor.fetchall():
    print(row)

# 2. Only students enrolled in Python, using WHERE on the joined result
print("\n2. Students enrolled in Python:")
cursor.execute("""
    SELECT Student.Name, Course.CourseName
    FROM Student
    INNER JOIN Course
    ON Student.CourseID = Course.CourseID
    WHERE Course.CourseName = 'Python'
""")
for row in cursor.fetchall():
    print(row)

# 3. Create a view for Python students
cursor.execute("""
    CREATE VIEW PythonStudents AS
    SELECT Student.Name, Course.CourseName
    FROM Student
    INNER JOIN Course
    ON Student.CourseID = Course.CourseID
    WHERE Course.CourseName = 'Python'
""")

print("\n3. View 'PythonStudents' created successfully")
print("Data from the view:")
cursor.execute("SELECT * FROM PythonStudents")
for row in cursor.fetchall():
    print(row)

connection.close()