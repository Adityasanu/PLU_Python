import sqlite3


# -----------------------------------
# 1. Student Class
# -----------------------------------

class Student:
    def __init__(self, roll_number, name, cgpa, skills, placement_status):
        self.roll_number = roll_number
        self.name = name
        self.cgpa = cgpa
        self.skills = skills
        self.placement_status = placement_status

    def display(self):
        print(
            self.roll_number,
            self.name,
            self.cgpa,
            self.skills,
            self.placement_status
        )


# -----------------------------------
# 2. Heapify Function
# -----------------------------------

def heapify(students, n, i):

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and students[left].cgpa > students[largest].cgpa:
        largest = left

    if right < n and students[right].cgpa > students[largest].cgpa:
        largest = right

    if largest != i:

        students[i], students[largest] = students[largest], students[i]

        heapify(students, n, largest)


# -----------------------------------
# 3. Heap Sort by CGPA
# -----------------------------------

def heap_sort(students):

    n = len(students)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(students, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):

        students[0], students[i] = students[i], students[0]

        heapify(students, i, 0)

    return students


# -----------------------------------
# 4. Binary Search by Roll Number
# -----------------------------------

def binary_search(students, target_roll):

    low = 0
    high = len(students) - 1

    while low <= high:

        mid = (low + high) // 2

        if students[mid].roll_number == target_roll:
            return students[mid]

        elif students[mid].roll_number < target_roll:
            low = mid + 1

        else:
            high = mid - 1

    return None


# -----------------------------------
# 5. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()


# -----------------------------------
# 6. Create Students Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    cgpa REAL,
    skills TEXT,
    placement_status TEXT
)
""")


# -----------------------------------
# 7. Insert Sample Students
# -----------------------------------

students = [
    (101, "Rahul", 8.2, "Python, SQL", "Not Placed"),
    (102, "Priya", 9.1, "Java, DSA", "Not Placed"),
    (103, "Aman", 7.2, "C++, Python", "Not Placed"),
    (104, "Neha", 8.7, "Web Development", "Not Placed"),
    (105, "Rohit", 6.9, "Java, SQL", "Not Placed"),
    (106, "Anjali", 7.8, "Python, DSA", "Not Placed")
]

cursor.executemany("""
INSERT OR IGNORE INTO students
(roll_number, name, cgpa, skills, placement_status)
VALUES (?, ?, ?, ?, ?)
""", students)

conn.commit()


# -----------------------------------
# 8. Retrieve All Students
# -----------------------------------

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()


# -----------------------------------
# 9. Convert Rows to Student Objects
# -----------------------------------

student_objects = []

for row in rows:

    student = Student(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4]
    )

    student_objects.append(student)


print("\nAll Students:")

for student in student_objects:
    student.display()


# -----------------------------------
# 10. Heap Sort by CGPA
# -----------------------------------

# Copy list so original data is preserved
students_by_cgpa = student_objects.copy()

heap_sort(students_by_cgpa)

print("\nStudents sorted by CGPA:")

for student in students_by_cgpa:
    student.display()


# -----------------------------------
# 11. Search Student by Roll Number
# -----------------------------------

# Binary Search requires sorted Roll Numbers
students_by_roll = sorted(
    student_objects,
    key=lambda student: student.roll_number
)

target_roll = int(
    input("\nEnter Roll Number to search: ")
)

found_student = binary_search(
    students_by_roll,
    target_roll
)

if found_student:

    print("\nStudent found:")
    found_student.display()

else:

    print("\nStudent not found.")


# -----------------------------------
# 12. Display Placement Eligible Students
# CGPA > 7.5
# -----------------------------------

print("\nStudents eligible for placement:")

for student in student_objects:

    if student.cgpa > 7.5:
        student.display()


# -----------------------------------
# 13. Update Placement Status
# -----------------------------------

selected_roll = int(
    input("\nEnter Roll Number of selected student: ")
)

cursor.execute("""
UPDATE students
SET placement_status = 'Placed'
WHERE roll_number = ?
""", (selected_roll,))

conn.commit()


# Check whether a student was actually updated
if cursor.rowcount > 0:

    print("\nPlacement status updated successfully.")

    cursor.execute("""
    SELECT *
    FROM students
    WHERE roll_number = ?
    """, (selected_roll,))

    updated_student = cursor.fetchone()

    print("\nUpdated Student:")

    print(
        updated_student[0],
        updated_student[1],
        updated_student[2],
        updated_student[3],
        updated_student[4]
    )

else:

    print("\nStudent not found.")


# -----------------------------------
# 14. Close Database
# -----------------------------------

conn.close()