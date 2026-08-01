'''Question 1
A company wants to store employee information.
Create the following table.
Employee
| Column Name | Data Type |
| ------------ | ------------ |
| EmployeeID | INT |
| EmployeeName | VARCHAR(100) |
| Department | VARCHAR(50) |
| Salary | INT |
| JoiningDate | DATE |
Tasks
1. Create the table.
2. Make 'EmployeeID' the Primary Key.
'''

import sqlite3

# using sqlite3 so this file can run directly and show real output
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Step 1: Create the table
# EmployeeID is set as PRIMARY KEY so every employee has a unique id
cursor.execute("""
    CREATE TABLE Employee (
        EmployeeID INT PRIMARY KEY,
        EmployeeName VARCHAR(100),
        Department VARCHAR(50),
        Salary INT,
        JoiningDate DATE
    )
""")

print("Employee table created successfully")

# just checking the table structure to confirm Primary Key is applied
cursor.execute("PRAGMA table_info(Employee)")
columns = cursor.fetchall()

print("\nTable structure:")
for col in columns:
    # col format -> (cid, name, type, notnull, default, pk)
    is_primary = "PRIMARY KEY" if col[5] == 1 else ""
    print(col[1], "-", col[2], is_primary)

connection.close()