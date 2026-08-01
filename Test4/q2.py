'''Question 2
Consider the following table.
Student
| StudentID | Name | Course | Marks |
| --------- | ----- | ------ | ----- |
| 101 | Rahul | Python | 80 |
| 102 | Priya | Java | 75 |
| 103 | Aman | Python | 90 |
| 104 | Neha | SQL | 70 |
Write SQL queries to:
1. Display all student records.
2. Display only Name and Marks.
3. Display only the Course column.'''

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE Student (
        StudentID INT,
        Name VARCHAR(50),
        Course VARCHAR(50),
        Marks INT
    )
""")

# inserting the given data
students = [
    (101, "Rahul", "Python", 80),
    (102, "Priya", "Java", 75),
    (103, "Aman", "Python", 90),
    (104, "Neha", "SQL", 70)
]
cursor.executemany("INSERT INTO Student VALUES (?, ?, ?, ?)", students)

# 1. Display all student records
print("1. All student records:")
cursor.execute("SELECT * FROM Student")
for row in cursor.fetchall():
    print(row)

# 2. Display only Name and Marks
print("\n2. Name and Marks only:")
cursor.execute("SELECT Name, Marks FROM Student")
for row in cursor.fetchall():
    print(row)

# 3. Display only the Course column
print("\n3. Course column only:")
cursor.execute("SELECT Course FROM Student")
for row in cursor.fetchall():
    print(row[0])

connection.close()
