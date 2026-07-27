import sqlite3
from datetime import datetime


# -----------------------------------
# 1. Employee Class
# -----------------------------------

class Employee:
    def __init__(self, employee_id, name, check_in, check_out):
        self.employee_id = employee_id
        self.name = name
        self.check_in = check_in
        self.check_out = check_out
        self.total_hours = 0

    def calculate_hours(self):
        check_in_time = datetime.strptime(
            self.check_in,
            "%Y-%m-%d %H:%M"
        )

        check_out_time = datetime.strptime(
            self.check_out,
            "%Y-%m-%d %H:%M"
        )

        difference = check_out_time - check_in_time

        self.total_hours = difference.total_seconds() / 3600

    def display(self):
        print(
            self.employee_id,
            self.name,
            "Hours:",
            round(self.total_hours, 2)
        )


# -----------------------------------
# 2. Binary Search by Employee ID
# -----------------------------------

def binary_search(employees, target_id):

    low = 0
    high = len(employees) - 1

    while low <= high:

        mid = (low + high) // 2

        if employees[mid].employee_id == target_id:
            return employees[mid]

        elif employees[mid].employee_id < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# -----------------------------------
# 3. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("attendance.db")

cursor = conn.cursor()


# -----------------------------------
# 4. Create Attendance Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    check_in TEXT,
    check_out TEXT
)
""")


# -----------------------------------
# 5. Insert Sample Attendance Data
# -----------------------------------

attendance_data = [
    (101, "Rahul", "2026-07-20 09:00", "2026-07-22 08:00"),
    (102, "Priya", "2026-07-20 09:00", "2026-07-22 10:00"),
    (103, "Aman", "2026-07-20 09:00", "2026-07-21 18:00"),
    (104, "Neha", "2026-07-20 08:00", "2026-07-22 09:00"),
    (105, "Rohit", "2026-07-20 09:00", "2026-07-21 17:00")
]

cursor.executemany("""
INSERT OR IGNORE INTO attendance
(employee_id, name, check_in, check_out)
VALUES (?, ?, ?, ?)
""", attendance_data)

conn.commit()


# -----------------------------------
# 6. Retrieve Attendance Records
# -----------------------------------

cursor.execute("SELECT * FROM attendance")

rows = cursor.fetchall()


# -----------------------------------
# 7. Convert Rows into Employee Objects
# -----------------------------------

employee_objects = []

for row in rows:

    employee = Employee(
        row[0],
        row[1],
        row[2],
        row[3]
    )

    employee.calculate_hours()

    employee_objects.append(employee)


# -----------------------------------
# 8. Display Attendance Records
# -----------------------------------

print("\nEmployee Attendance Records:")

for employee in employee_objects:
    employee.display()


# -----------------------------------
# 9. Sort by Total Hours Worked
# -----------------------------------

employees_by_hours = sorted(
    employee_objects,
    key=lambda employee: employee.total_hours,
    reverse=True
)

print("\nEmployees sorted by Total Hours:")

for employee in employees_by_hours:
    employee.display()


# -----------------------------------
# 10. Search Employee using ID
# -----------------------------------

employees_by_id = sorted(
    employee_objects,
    key=lambda employee: employee.employee_id
)

target_id = int(
    input("\nEnter Employee ID to search: ")
)

found_employee = binary_search(
    employees_by_id,
    target_id
)

if found_employee:

    print("\nEmployee Found:")
    found_employee.display()

else:

    print("\nEmployee not found.")


# -----------------------------------
# 11. Employees Working > 45 Hours
# -----------------------------------

print("\nEmployees who worked more than 45 hours:")

found = False

for employee in employee_objects:

    if employee.total_hours > 45:
        employee.display()
        found = True

if not found:
    print("No employee worked more than 45 hours.")


# -----------------------------------
# 12. Close Database
# -----------------------------------

conn.close()