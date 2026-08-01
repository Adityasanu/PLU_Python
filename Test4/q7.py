'''Question 7
Consider the following table.
Employee
| EmployeeID | Name | Department | Salary |
| ---------- | ----- | ---------- | ------ |
| 1 | Rahul | IT | 65000 |
| 2 | Priya | HR | 45000 |
| 3 | Aman | IT | 70000 |
Create a view named `HighSalaryEmployees` that displays employees earning
more than ₹60,000.
'''

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE Employee (
        EmployeeID INT,
        Name VARCHAR(50),
        Department VARCHAR(50),
        Salary INT
    )
""")

employees = [
    (1, "Rahul", "IT", 65000),
    (2, "Priya", "HR", 45000),
    (3, "Aman", "IT", 70000)
]
cursor.executemany("INSERT INTO Employee VALUES (?, ?, ?, ?)", employees)

# a view is like a saved query, it does not store data on its own,
# it just shows the result of the query whenever we select from it
cursor.execute("""
    CREATE VIEW HighSalaryEmployees AS
    SELECT * FROM Employee WHERE Salary > 60000
""")

print("View 'HighSalaryEmployees' created successfully")

print("\nData from the view:")
cursor.execute("SELECT * FROM HighSalaryEmployees")
for row in cursor.fetchall():
    print(row)

connection.close()