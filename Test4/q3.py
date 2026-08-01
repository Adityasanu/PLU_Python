'''Question 3
Consider the following table.
Product
| ProductID | ProductName | Category | Price |
| --------- | ----------- | ----------- | ----- |
| 1 | Mouse | Electronics | 800 |
| 2 | Laptop | Electronics | 65000 |
| 3 | Chair | Furniture | 4500 |
| 4 | Keyboard | Electronics | 1200 |
Write SQL queries to:
1. Display products costing more than ₹1000.
2. Display all Electronics products.
3. Display the Laptop record.'''

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE Product (
        ProductID INT,
        ProductName VARCHAR(50),
        Category VARCHAR(50),
        Price INT
    )
""")

products = [
    (1, "Mouse", "Electronics", 800),
    (2, "Laptop", "Electronics", 65000),
    (3, "Chair", "Furniture", 4500),
    (4, "Keyboard", "Electronics", 1200)
]
cursor.executemany("INSERT INTO Product VALUES (?, ?, ?, ?)", products)

# 1. Products costing more than 1000
print("1. Products costing more than 1000:")
cursor.execute("SELECT * FROM Product WHERE Price > 1000")
for row in cursor.fetchall():
    print(row)

# 2. All Electronics products
print("\n2. Electronics products:")
cursor.execute("SELECT * FROM Product WHERE Category = 'Electronics'")
for row in cursor.fetchall():
    print(row)

# 3. The Laptop record
print("\n3. Laptop record:")
cursor.execute("SELECT * FROM Product WHERE ProductName = 'Laptop'")
for row in cursor.fetchall():
    print(row)

connection.close()
