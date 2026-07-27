import sqlite3
from datetime import datetime, timedelta


# -----------------------------------
# 1. Book Class
# -----------------------------------

class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def display(self):
        print(
            self.book_id,
            self.title,
            self.author,
            self.availability
        )


# -----------------------------------
# 2. Merge Sort
# Sort Books Alphabetically by Title
# -----------------------------------

def merge_sort(books):

    if len(books) <= 1:
        return books

    mid = len(books) // 2

    left = merge_sort(books[:mid])
    right = merge_sort(books[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].title.lower() <= right[j].title.lower():

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------------
# 3. Binary Search by Book ID
# -----------------------------------

def binary_search(books, target_id):

    low = 0
    high = len(books) - 1

    while low <= high:

        mid = (low + high) // 2

        if books[mid].book_id == target_id:
            return books[mid]

        elif books[mid].book_id < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# -----------------------------------
# 4. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("library.db")

cursor = conn.cursor()


# -----------------------------------
# 5. Create Books Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    availability TEXT
)
""")


# -----------------------------------
# 6. Create Members Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY,
    member_name TEXT NOT NULL
)
""")


# -----------------------------------
# 7. Create Borrowed Books Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS borrowed_books (
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    borrow_date TEXT,
    due_date TEXT,
    return_date TEXT,

    FOREIGN KEY (book_id)
        REFERENCES books(book_id),

    FOREIGN KEY (member_id)
        REFERENCES members(member_id)
)
""")


# -----------------------------------
# 8. Insert Sample Books
# -----------------------------------

books = [
    (101, "Python Basics", "John Smith", "Available"),
    (102, "Data Structures", "Mark Allen", "Available"),
    (103, "Database Systems", "David Lee", "Available"),
    (104, "Computer Networks", "James Brown", "Available"),
    (105, "Operating Systems", "Robert Martin", "Available")
]

cursor.executemany("""
INSERT OR IGNORE INTO books
(book_id, title, author, availability)
VALUES (?, ?, ?, ?)
""", books)


# -----------------------------------
# 9. Insert Sample Members
# -----------------------------------

members = [
    (201, "Rahul"),
    (202, "Priya"),
    (203, "Aman")
]

cursor.executemany("""
INSERT OR IGNORE INTO members
(member_id, member_name)
VALUES (?, ?)
""", members)

conn.commit()


# -----------------------------------
# 10. Display Available Books
# -----------------------------------

cursor.execute("""
SELECT *
FROM books
WHERE availability = 'Available'
""")

rows = cursor.fetchall()

book_objects = []

for row in rows:

    book = Book(
        row[0],
        row[1],
        row[2],
        row[3]
    )

    book_objects.append(book)


print("\nAvailable Books:")

for book in book_objects:
    book.display()


# -----------------------------------
# 11. Merge Sort Alphabetically
# -----------------------------------

sorted_books = merge_sort(book_objects)

print("\nBooks Sorted Alphabetically:")

for book in sorted_books:
    book.display()


# -----------------------------------
# 12. Search Book by Book ID
# -----------------------------------

books_by_id = sorted(
    book_objects,
    key=lambda book: book.book_id
)

target_id = int(
    input("\nEnter Book ID to search: ")
)

found_book = binary_search(
    books_by_id,
    target_id
)

if found_book:

    print("\nBook Found:")
    found_book.display()

else:

    print("\nBook not found.")


# -----------------------------------
# 13. Borrow a Book
# -----------------------------------

borrow_book_id = int(
    input("\nEnter Book ID to borrow: ")
)

member_id = int(
    input("Enter Member ID: ")
)


# Check if Book is Available

cursor.execute("""
SELECT availability
FROM books
WHERE book_id = ?
""", (borrow_book_id,))

book_status = cursor.fetchone()


if book_status is None:

    print("\nBook does not exist.")


elif book_status[0] != "Available":

    print("\nBook is not available.")


else:

    # Current date
    borrow_date = datetime.now()

    # Book must be returned within 14 days
    due_date = borrow_date + timedelta(days=14)


    # -----------------------------------
    # 14. Add Borrowing Record
    # -----------------------------------

    cursor.execute("""
    INSERT INTO borrowed_books
    (
        book_id,
        member_id,
        borrow_date,
        due_date,
        return_date
    )
    VALUES (?, ?, ?, ?, NULL)
    """, (
        borrow_book_id,
        member_id,
        borrow_date.strftime("%Y-%m-%d"),
        due_date.strftime("%Y-%m-%d")
    ))


    # -----------------------------------
    # 15. Update Book Availability
    # -----------------------------------

    cursor.execute("""
    UPDATE books
    SET availability = 'Borrowed'
    WHERE book_id = ?
    """, (borrow_book_id,))

    conn.commit()

    print("\nBook borrowed successfully.")
    print(
        "Due Date:",
        due_date.strftime("%Y-%m-%d")
    )


# -----------------------------------
# 16. Display Overdue Books
# -----------------------------------

today = datetime.now().strftime("%Y-%m-%d")

cursor.execute("""
SELECT
    books.book_id,
    books.title,
    members.member_name,
    borrowed_books.due_date
FROM borrowed_books

JOIN books
ON borrowed_books.book_id = books.book_id

JOIN members
ON borrowed_books.member_id = members.member_id

WHERE borrowed_books.due_date < ?
AND borrowed_books.return_date IS NULL
""", (today,))

overdue_books = cursor.fetchall()


print("\nOverdue Books:")

if overdue_books:

    for book in overdue_books:

        print(
            "Book ID:", book[0],
            "| Title:", book[1],
            "| Member:", book[2],
            "| Due Date:", book[3]
        )

else:

    print("No overdue books.")


# -----------------------------------
# 17. Close Database
# -----------------------------------

conn.close()