import sqlite3


# -----------------------------------
# 1. Transaction Class
# -----------------------------------

class Transaction:
    def __init__(self, transaction_id, account_number, amount, date, transaction_type):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.amount = amount
        self.date = date
        self.transaction_type = transaction_type

    def display(self):
        print(
            self.transaction_id,
            self.account_number,
            self.amount,
            self.date,
            self.transaction_type
        )


# -----------------------------------
# 2. Quick Sort by Amount
# -----------------------------------

def quick_sort(transactions):

    if len(transactions) <= 1:
        return transactions

    pivot = transactions[len(transactions) // 2]

    left = []
    middle = []
    right = []

    for transaction in transactions:

        if transaction.amount < pivot.amount:
            left.append(transaction)

        elif transaction.amount == pivot.amount:
            middle.append(transaction)

        else:
            right.append(transaction)

    return quick_sort(left) + middle + quick_sort(right)


# -----------------------------------
# 3. Binary Search by Transaction ID
# -----------------------------------

def binary_search(transactions, target_id):

    low = 0
    high = len(transactions) - 1

    while low <= high:

        mid = (low + high) // 2

        if transactions[mid].transaction_id == target_id:
            return transactions[mid]

        elif transactions[mid].transaction_id < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# -----------------------------------
# 4. Connect to SQLite
# -----------------------------------

conn = sqlite3.connect("bank.db")

cursor = conn.cursor()


# -----------------------------------
# 5. Create Transactions Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_number TEXT NOT NULL,
    amount REAL,
    date TEXT,
    type TEXT
)
""")


# -----------------------------------
# 6. Insert Sample Transactions
# -----------------------------------

transactions = [
    (101, "ACC1001", 5000, "2026-07-01", "Credit"),
    (102, "ACC1002", 2500, "2026-07-02", "Debit"),
    (103, "ACC1003", 10000, "2026-07-03", "Credit"),
    (104, "ACC1001", 1500, "2026-07-04", "Debit"),
    (105, "ACC1004", 7500, "2026-07-05", "Credit"),
    (106, "ACC1002", 3000, "2026-07-06", "Debit"),
    (107, "ACC1005", 12000, "2026-07-07", "Credit")
]

cursor.executemany("""
INSERT OR IGNORE INTO transactions
(transaction_id, account_number, amount, date, type)
VALUES (?, ?, ?, ?, ?)
""", transactions)

conn.commit()


# -----------------------------------
# 7. Retrieve All Transactions
# -----------------------------------

cursor.execute("SELECT * FROM transactions")

rows = cursor.fetchall()


# -----------------------------------
# 8. Convert Rows to Python Objects
# -----------------------------------

transaction_objects = []

for row in rows:

    transaction = Transaction(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4]
    )

    transaction_objects.append(transaction)


print("\nAll Transactions:")

for transaction in transaction_objects:
    transaction.display()


# -----------------------------------
# 9. Quick Sort by Amount
# -----------------------------------

sorted_transactions = quick_sort(transaction_objects)

print("\nTransactions sorted by amount:")

for transaction in sorted_transactions:
    transaction.display()


# -----------------------------------
# 10. Search by Transaction ID
# -----------------------------------

# Binary Search requires data sorted
# according to Transaction ID

transactions_by_id = sorted(
    transaction_objects,
    key=lambda transaction: transaction.transaction_id
)

target_id = int(
    input("\nEnter Transaction ID to search: ")
)

found_transaction = binary_search(
    transactions_by_id,
    target_id
)

if found_transaction:

    print("\nTransaction found:")
    found_transaction.display()

else:

    print("\nTransaction not found.")


# -----------------------------------
# 11. Calculate Total Credits/Debits
# -----------------------------------

total_credit = 0
total_debit = 0

for transaction in transaction_objects:

    if transaction.transaction_type == "Credit":
        total_credit += transaction.amount

    elif transaction.transaction_type == "Debit":
        total_debit += transaction.amount


print("\nTotal Credit:", total_credit)
print("Total Debit:", total_debit)


# -----------------------------------
# 12. Top 5 Highest Transactions
# -----------------------------------

print("\nTop 5 Highest-Value Transactions:")

top_five = sorted_transactions[-5:]

# Reverse so highest amount appears first
top_five.reverse()

for transaction in top_five:
    transaction.display()


# -----------------------------------
# 13. Close Database
# -----------------------------------

conn.close()