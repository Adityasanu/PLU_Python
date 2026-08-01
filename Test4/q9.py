'''Question 9
Consider the following table.
Book
| BookID | BookName | Author | Price |
| ------ | ------------- | ------ | ----- |
| 1 | Python Basics | John | 500 |
| 2 | Learning SQL | David | 700 |
Write a stored procedure named 'GetBooks' that displays all records from the
Book table.
'''

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE Book (
        BookID INT,
        BookName VARCHAR(50),
        Author VARCHAR(50),
        Price INT
    )
""")

books = [
    (1, "Python Basics", "John", 500),
    (2, "Learning SQL", "David", 700)
]
cursor.executemany("INSERT INTO Book VALUES (?, ?, ?, ?)", books)


def GetBooks():
    cursor.execute("SELECT * FROM Book")
    return cursor.fetchall()


print("Calling GetBooks():")
for row in GetBooks():
    print(row)

connection.close()