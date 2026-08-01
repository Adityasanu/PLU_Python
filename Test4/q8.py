'''Question 8
Consider the following table.
Orders
| OrderID | CustomerName | OrderDate | Amount |
| ------- | ------------ | --------- | ------ |
Tasks
1. Create an index on OrderID.
2. Explain one benefit of creating an index.
'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE Orders (
        OrderID INT,
        CustomerName VARCHAR(50),
        OrderDate DATE,
        Amount INT
    )
""")

# Step 1: Create an index on OrderID
cursor.execute("CREATE INDEX idx_orderid ON Orders(OrderID)")

print("Index 'idx_orderid' created successfully on OrderID")

# confirming the index actually exists
cursor.execute("PRAGMA index_list(Orders)")
print("\nIndexes on Orders table:")
for row in cursor.fetchall():
    print(row)

# Step 2: Benefit of creating an index
print("""
2. Benefit of creating an index:
- An index helps the database find rows much faster when we search or
  filter using that column (for example, WHERE OrderID = 5).
- Without an index, the database has to check every single row one by one,
  but with an index it can jump directly to the matching rows, similar to
  how an index page in a book helps us find a topic quickly instead of
  reading the whole book.
""")

connection.close()