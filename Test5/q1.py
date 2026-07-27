import sqlite3


# -----------------------------------
# 1. Product Class
# -----------------------------------

class Product:
    def __init__(self, product_id, product_name, category, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.quantity = quantity
        self.price = price

    def display(self):
        print(
            self.product_id,
            self.product_name,
            self.category,
            self.quantity,
            self.price
        )


# -----------------------------------
# 2. Merge Sort
# Sort products based on quantity
# -----------------------------------

def merge_sort(products):

    if len(products) <= 1:
        return products

    mid = len(products) // 2

    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].quantity <= right[j].quantity:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------------
# 3. Binary Search
# Search using Product ID
# -----------------------------------

def binary_search(products, target_id):

    low = 0
    high = len(products) - 1

    while low <= high:

        mid = (low + high) // 2

        if products[mid].product_id == target_id:
            return products[mid]

        elif products[mid].product_id < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# -----------------------------------
# 4. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("inventory.db")

cursor = conn.cursor()


# -----------------------------------
# 5. Create Products Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    quantity INTEGER,
    price REAL
)
""")


# -----------------------------------
# 6. Insert Sample Products
# -----------------------------------

products = [
    (101, "Laptop", "Electronics", 8, 65000),
    (102, "Mouse", "Electronics", 25, 800),
    (103, "Keyboard", "Electronics", 6, 1500),
    (104, "Chair", "Furniture", 15, 5000),
    (105, "Headphones", "Electronics", 4, 2500)
]

cursor.executemany("""
INSERT OR IGNORE INTO products
(product_id, product_name, category, quantity, price)
VALUES (?, ?, ?, ?, ?)
""", products)

conn.commit()


# -----------------------------------
# 7. Fetch Products from Database
# -----------------------------------

cursor.execute("SELECT * FROM products")

rows = cursor.fetchall()


# -----------------------------------
# 8. Convert Database Rows
# into Python Product Objects
# -----------------------------------

product_objects = []

for row in rows:

    product = Product(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4]
    )

    product_objects.append(product)


# -----------------------------------
# 9. Merge Sort by Quantity
# -----------------------------------

sorted_products = merge_sort(product_objects)

print("\nProducts sorted by quantity:")

for product in sorted_products:
    product.display()


# -----------------------------------
# 10. Binary Search by Product ID
# -----------------------------------

# Binary Search requires Product IDs
# to be in sorted order
products_by_id = sorted(
    product_objects,
    key=lambda product: product.product_id
)

target_id = int(input("\nEnter Product ID to search: "))

found_product = binary_search(products_by_id, target_id)

if found_product:

    print("\nProduct found:")
    found_product.display()

else:

    print("\nProduct not found.")


# -----------------------------------
# 11. Close Database
# -----------------------------------
print("\nProducts with stock below 10:")

for product in product_objects:
    if product.quantity < 10:
        product.display()
        
conn.close()