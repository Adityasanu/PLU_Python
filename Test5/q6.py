import sqlite3
from collections import deque


# -----------------------------------
# 1. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("food_delivery.db")

cursor = conn.cursor()


# -----------------------------------
# 2. Create Restaurant Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurant (
    restaurant_id INTEGER PRIMARY KEY,
    restaurant_name TEXT NOT NULL,
    location TEXT
)
""")


# -----------------------------------
# 3. Create Delivery Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS delivery (
    delivery_id INTEGER PRIMARY KEY,
    delivery_location TEXT,
    status TEXT
)
""")


# -----------------------------------
# 4. Create Orders Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    delivery_id INTEGER,
    status TEXT,
    FOREIGN KEY (restaurant_id)
        REFERENCES restaurant(restaurant_id),
    FOREIGN KEY (delivery_id)
        REFERENCES delivery(delivery_id)
)
""")


# -----------------------------------
# 5. Insert Restaurant Data
# -----------------------------------

restaurants = [
    (1, "Pizza Hub", "A"),
    (2, "Burger Point", "B"),
    (3, "Food Corner", "C")
]

cursor.executemany("""
INSERT OR IGNORE INTO restaurant
(restaurant_id, restaurant_name, location)
VALUES (?, ?, ?)
""", restaurants)


# -----------------------------------
# 6. Insert Delivery Locations
# -----------------------------------

deliveries = [
    (101, "D", "Pending"),
    (102, "E", "Pending"),
    (103, "F", "Pending")
]

cursor.executemany("""
INSERT OR IGNORE INTO delivery
(delivery_id, delivery_location, status)
VALUES (?, ?, ?)
""", deliveries)


# -----------------------------------
# 7. Insert Orders
# -----------------------------------

orders = [
    (1001, 1, 101, "Pending"),
    (1002, 2, 102, "Pending"),
    (1003, 3, 103, "Pending")
]

cursor.executemany("""
INSERT OR IGNORE INTO orders
(order_id, restaurant_id, delivery_id, status)
VALUES (?, ?, ?, ?)
""", orders)

conn.commit()


# -----------------------------------
# 8. Fetch Pending Orders using JOIN
# -----------------------------------

cursor.execute("""
SELECT
    orders.order_id,
    restaurant.restaurant_name,
    restaurant.location,
    delivery.delivery_location
FROM orders
JOIN restaurant
ON orders.restaurant_id = restaurant.restaurant_id
JOIN delivery
ON orders.delivery_id = delivery.delivery_id
WHERE orders.status = 'Pending'
""")

pending_orders = cursor.fetchall()


print("\nPending Orders:")

for order in pending_orders:
    print(
        "Order ID:", order[0],
        "| Restaurant:", order[1],
        "| From:", order[2],
        "| To:", order[3]
    )


# -----------------------------------
# 9. Create Graph
# -----------------------------------

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


# -----------------------------------
# 10. BFS Function
# Find Shortest Path
# -----------------------------------

def bfs(graph, start, destination):

    queue = deque()

    queue.append([start])

    visited = set()

    while queue:

        path = queue.popleft()

        current_location = path[-1]

        if current_location == destination:
            return path

        if current_location not in visited:

            visited.add(current_location)

            for neighbour in graph[current_location]:

                new_path = path + [neighbour]

                queue.append(new_path)

    return None


# -----------------------------------
# 11. Find Delivery Paths
# -----------------------------------

print("\nDelivery Routes:")

for order in pending_orders:

    order_id = order[0]
    restaurant_name = order[1]
    start = order[2]
    destination = order[3]

    shortest_path = bfs(
        graph,
        start,
        destination
    )

    print(
        "\nOrder:",
        order_id,
        "-",
        restaurant_name
    )

    if shortest_path:

        print(
            "Shortest Path:",
            " -> ".join(shortest_path)
        )

    else:

        print("No route found.")


# -----------------------------------
# 12. Display Delivery Order Sequence
# -----------------------------------

print("\nDelivery Order Sequence:")

for order in pending_orders:
    print("Order", order[0])


# -----------------------------------
# 13. Mark Deliveries as Completed
# -----------------------------------

for order in pending_orders:

    order_id = order[0]

    cursor.execute("""
    UPDATE orders
    SET status = 'Completed'
    WHERE order_id = ?
    """, (order_id,))


conn.commit()

print("\nAll pending deliveries marked as Completed.")


# -----------------------------------
# 14. Display Updated Orders
# -----------------------------------

cursor.execute("""
SELECT order_id, status
FROM orders
""")

updated_orders = cursor.fetchall()

print("\nUpdated Order Status:")

for order in updated_orders:

    print(
        "Order:",
        order[0],
        "| Status:",
        order[1]
    )


# -----------------------------------
# 15. Close Database
# -----------------------------------

conn.close()