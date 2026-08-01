'''Question 5
Consider the following tables.
Employee
| EmployeeID | Name | DepartmentID |
| ---------- | ----- | ------------ |
| 1 | Rahul | 101 |
| 2 | Priya | 102 |
| 3 | Aman | 101 |
Department
| DepartmentID | DepartmentName |
| ------------ | -------------- |
| 101 | IT |
| 102 | HR |
Write an SQL query to display
* Employee Name
* Department Name
using an INNER JOIN.'''


import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE Employee (
        EmployeeID INT,
        Name VARCHAR(50),
        DepartmentID INT
    )
""")

cursor.execute("""
    CREATE TABLE Department (
        DepartmentID INT,
        DepartmentName VARCHAR(50)
    )
""")

employees = [
    (1, "Rahul", 101),
    (2, "Priya", 102),
    (3, "Aman", 101)
]
cursor.executemany("INSERT INTO Employee VALUES (?, ?, ?)", employees)

departments = [
    (101, "IT"),
    (102, "HR")
]
cursor.executemany("INSERT INTO Department VALUES (?, ?)", departments)

# INNER JOIN only shows rows where DepartmentID matches in both tables
print("Employee Name and Department Name (INNER JOIN):")
cursor.execute("""
    SELECT Employee.Name, Department.DepartmentName
    FROM Employee
    INNER JOIN Department
    ON Employee.DepartmentID = Department.DepartmentID
""")
for row in cursor.fetchall():
    print(row)

connection.close()
