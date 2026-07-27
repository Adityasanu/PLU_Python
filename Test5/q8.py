import sqlite3
from collections import deque


# -----------------------------------
# 1. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("ride_booking.db")

cursor = conn.cursor()


# -----------------------------------
# 2. Create Drivers Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INTEGER PRIMARY KEY,
    driver_name TEXT NOT NULL,
    location TEXT,
    availability TEXT
)
""")


# -----------------------------------
# 3. Create Customers Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    location TEXT
)
""")


# -----------------------------------
# 4. Create Bookings Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    driver_id INTEGER,
    status TEXT,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (driver_id)
        REFERENCES drivers(driver_id)
)
""")


# -----------------------------------
# 5. Insert Driver Data
# -----------------------------------

drivers = [
    (101, "Rahul", "A", "Available"),
    (102, "Aman", "C", "Available"),
    (103, "Rohit", "E", "Available"),
    (104, "Karan", "F", "Not Available")
]

cursor.executemany("""
INSERT OR IGNORE INTO drivers
(driver_id, driver_name, location, availability)
VALUES (?, ?, ?, ?)
""", drivers)


# -----------------------------------
# 6. Insert Customer Data
# -----------------------------------

customers = [
    (201, "Priya", "B"),
    (202, "Neha", "D"),
    (203, "Anjali", "F")
]

cursor.executemany("""
INSERT OR IGNORE INTO customers
(customer_id, customer_name, location)
VALUES (?, ?, ?)
""", customers)


# -----------------------------------
# 7. Insert Booking
# -----------------------------------

bookings = [
    (1001, 201, None, "Pending")
]

cursor.executemany("""
INSERT OR IGNORE INTO bookings
(booking_id, customer_id, driver_id, status)
VALUES (?, ?, ?, ?)
""", bookings)

conn.commit()


# -----------------------------------
# 8. Fetch Available Drivers
# -----------------------------------

cursor.execute("""
SELECT *
FROM drivers
WHERE availability = 'Available'
""")

available_drivers = cursor.fetchall()


print("\nAvailable Drivers:")

for driver in available_drivers:
    print(
        "ID:", driver[0],
        "| Name:", driver[1],
        "| Location:", driver[2]
    )


# -----------------------------------
# 9. Create City Graph
# -----------------------------------

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}


# -----------------------------------
# 10. BFS Function
# Find Distance Between Locations
# -----------------------------------

def bfs_distance(graph, start, destination):

    queue = deque()

    queue.append((start, 0))

    visited = set()

    while queue:

        current_location, distance = queue.popleft()

        if current_location == destination:
            return distance

        if current_location not in visited:

            visited.add(current_location)

            for neighbour in graph[current_location]:

                queue.append(
                    (neighbour, distance + 1)
                )

    return None


# -----------------------------------
# 11. Fetch Pending Booking
# Using SQL JOIN
# -----------------------------------

cursor.execute("""
SELECT
    bookings.booking_id,
    customers.customer_id,
    customers.customer_name,
    customers.location
FROM bookings
JOIN customers
ON bookings.customer_id = customers.customer_id
WHERE bookings.status = 'Pending'
""")

booking = cursor.fetchone()


# -----------------------------------
# 12. Find Nearest Driver using BFS
# -----------------------------------

if booking:

    booking_id = booking[0]
    customer_id = booking[1]
    customer_name = booking[2]
    customer_location = booking[3]

    print("\nBooking Details:")
    print("Booking ID:", booking_id)
    print("Customer:", customer_name)
    print("Customer Location:", customer_location)

    nearest_driver = None
    minimum_distance = float("inf")

    for driver in available_drivers:

        driver_id = driver[0]
        driver_name = driver[1]
        driver_location = driver[2]

        distance = bfs_distance(
            graph,
            customer_location,
            driver_location
        )

        if distance is not None and distance < minimum_distance:

            minimum_distance = distance
            nearest_driver = driver


    # -----------------------------------
    # 13. Assign Nearest Driver
    # -----------------------------------

    if nearest_driver:

        driver_id = nearest_driver[0]
        driver_name = nearest_driver[1]
        driver_location = nearest_driver[2]

        print("\nNearest Driver:")
        print("Driver ID:", driver_id)
        print("Driver Name:", driver_name)
        print("Driver Location:", driver_location)
        print("Distance:", minimum_distance)


        # -----------------------------------
        # 14. Update Booking
        # -----------------------------------

        cursor.execute("""
        UPDATE bookings
        SET driver_id = ?,
            status = 'Assigned'
        WHERE booking_id = ?
        """, (driver_id, booking_id))


        # -----------------------------------
        # 15. Update Driver Availability
        # -----------------------------------

        cursor.execute("""
        UPDATE drivers
        SET availability = 'Not Available'
        WHERE driver_id = ?
        """, (driver_id,))

        conn.commit()

        print("\nBooking assigned successfully.")
        print("Driver availability updated.")


# -----------------------------------
# 16. Display Updated Booking
# Using SQL JOIN
# -----------------------------------

cursor.execute("""
SELECT
    bookings.booking_id,
    customers.customer_name,
    drivers.driver_name,
    bookings.status
FROM bookings
JOIN customers
ON bookings.customer_id = customers.customer_id
LEFT JOIN drivers
ON bookings.driver_id = drivers.driver_id
""")

updated_bookings = cursor.fetchall()


print("\nUpdated Booking Details:")

for row in updated_bookings:

    print(
        "Booking ID:", row[0],
        "| Customer:", row[1],
        "| Driver:", row[2],
        "| Status:", row[3]
    )


# -----------------------------------
# 17. Close Database
# -----------------------------------

conn.close()