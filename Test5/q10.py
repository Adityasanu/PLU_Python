import sqlite3


# -----------------------------------
# 1. Sales Class
# -----------------------------------

class Sale:
    def __init__(
        self,
        salesperson_id,
        product,
        quantity,
        revenue,
        region,
        incentive_status
    ):
        self.salesperson_id = salesperson_id
        self.product = product
        self.quantity = quantity
        self.revenue = revenue
        self.region = region
        self.incentive_status = incentive_status

    def display(self):
        print(
            self.salesperson_id,
            self.product,
            self.quantity,
            self.revenue,
            self.region,
            self.incentive_status
        )


# -----------------------------------
# 2. Binary Search by Salesperson ID
# -----------------------------------

def binary_search(sales, target_id):

    low = 0
    high = len(sales) - 1

    while low <= high:

        mid = (low + high) // 2

        if sales[mid].salesperson_id == target_id:
            return sales[mid]

        elif sales[mid].salesperson_id < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# -----------------------------------
# 3. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("sales.db")

cursor = conn.cursor()


# -----------------------------------
# 4. Create Sales Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    salesperson_id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    quantity INTEGER,
    revenue REAL,
    region TEXT,
    incentive_status TEXT
)
""")


# -----------------------------------
# 5. Insert Sample Sales Data
# -----------------------------------

sales_data = [
    (101, "Laptop", 10, 650000, "North", "Not Eligible"),
    (102, "Mobile", 20, 500000, "South", "Not Eligible"),
    (103, "Tablet", 15, 450000, "East", "Not Eligible"),
    (104, "Laptop", 12, 780000, "West", "Not Eligible"),
    (105, "Headphones", 30, 150000, "North", "Not Eligible"),
    (106, "Monitor", 18, 360000, "South", "Not Eligible"),
    (107, "Keyboard", 25, 125000, "East", "Not Eligible"),
    (108, "Laptop", 14, 910000, "West", "Not Eligible")
]

cursor.executemany("""
INSERT OR IGNORE INTO sales
(
    salesperson_id,
    product,
    quantity,
    revenue,
    region,
    incentive_status
)
VALUES (?, ?, ?, ?, ?, ?)
""", sales_data)

conn.commit()


# -----------------------------------
# 6. Retrieve All Sales Records
# -----------------------------------

cursor.execute("SELECT * FROM sales")

rows = cursor.fetchall()


# -----------------------------------
# 7. Convert Rows into Sale Objects
# -----------------------------------

sale_objects = []

for row in rows:

    sale = Sale(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5]
    )

    sale_objects.append(sale)


print("\nAll Sales Records:")

for sale in sale_objects:
    sale.display()


# -----------------------------------
# 8. Sort Records by Revenue
# -----------------------------------

sales_by_revenue = sorted(
    sale_objects,
    key=lambda sale: sale.revenue,
    reverse=True
)

print("\nSales Sorted by Revenue:")

for sale in sales_by_revenue:
    sale.display()


# -----------------------------------
# 9. Search Salesperson by ID
# -----------------------------------

sales_by_id = sorted(
    sale_objects,
    key=lambda sale: sale.salesperson_id
)

target_id = int(
    input("\nEnter Salesperson ID to search: ")
)

found_sale = binary_search(
    sales_by_id,
    target_id
)

if found_sale:

    print("\nSalesperson Found:")
    found_sale.display()

else:

    print("\nSalesperson not found.")


# -----------------------------------
# 10. Display Top 5 Salespersons
# -----------------------------------

print("\nTop 5 Salespersons:")

top_five = sales_by_revenue[:5]

for sale in top_five:
    sale.display()


# -----------------------------------
# 11. Find Highest Revenue Region
# Using SQL GROUP BY
# -----------------------------------

cursor.execute("""
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC
LIMIT 1
""")

highest_region = cursor.fetchone()


if highest_region:

    print("\nHighest Revenue Region:")

    print(
        highest_region[0],
        "- Total Revenue:",
        highest_region[1]
    )


# -----------------------------------
# 12. Update Monthly Incentive Status
# -----------------------------------

# We assume salesperson is eligible
# if revenue is 500000 or more.

cursor.execute("""
UPDATE sales
SET incentive_status = 'Eligible'
WHERE revenue >= 500000
""")

conn.commit()


# -----------------------------------
# 13. Display Incentive Status
# -----------------------------------

cursor.execute("""
SELECT salesperson_id, revenue, incentive_status
FROM sales
""")

incentive_records = cursor.fetchall()


print("\nMonthly Incentive Status:")

for record in incentive_records:

    print(
        "Salesperson ID:", record[0],
        "| Revenue:", record[1],
        "| Status:", record[2]
    )


# -----------------------------------
# 14. Close Database
# -----------------------------------

conn.close()