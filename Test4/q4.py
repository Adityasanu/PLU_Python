'''Question 4
Create the following table.
Customer
| Column | Data Type |
| ------------ | ------------ |
| CustomerID | INT |
| CustomerName | VARCHAR(100) |
| City | VARCHAR(50) |
| Mobile | VARCHAR(15) |
Tasks
1. Create the table.
2. Make CustomerID the Primary Key.
3. Explain why Primary Keys are important.
'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Step 1 & 2: Create table with CustomerID as Primary Key
cursor.execute("""
    CREATE TABLE Customer (
        CustomerID INT PRIMARY KEY,
        CustomerName VARCHAR(100),
        City VARCHAR(50),
        Mobile VARCHAR(15)
    )
""")

print("Customer table created successfully")

# checking table structure to confirm the primary key
cursor.execute("PRAGMA table_info(Customer)")
columns = cursor.fetchall()

print("\nTable structure:")
for col in columns:
    is_primary = "PRIMARY KEY" if col[5] == 1 else ""
    print(col[1], "-", col[2], is_primary)

# Step 3: Why Primary Keys are important
print("""
3. Why Primary Keys are important:
- A Primary Key makes sure every row in the table is unique, so no two
  customers can have the same CustomerID.
- It does not allow NULL values, so every record must have an identifying value.
- It helps the database find and access records faster since it is indexed
  automatically.
- It is also used to link this table with other tables (for example,
  using CustomerID as a foreign key in an Orders table).
""")

connection.close()