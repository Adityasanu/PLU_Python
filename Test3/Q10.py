'''10. School Annual Report
A school has recorded the marks of 50 students.
Write a program that:
Sorts the marks in ascending order.
Accepts a mark from the user.
Checks whether that mark exists in the sorted list.
Displays the position if found; otherwise, prints "Mark Not Found."'''

# Approach:
# - This question combines both sorting and searching.
# - Step 1: The marks of 50 students are stored in random order,
#   so first we sort them in ascending order using Bubble Sort
#   (compare neighbours, swap if left is bigger, repeat).
# - Step 2: We ask the user to enter a mark they want to check.
# - Step 3: Since the list is now sorted, we use Binary Search
#   to look for that mark efficiently:
#     1. Check the middle mark.
#     2. If it matches, we found it.
#     3. If the middle mark is smaller, search the right half.
#     4. If the middle mark is bigger, search the left half.
#     5. Repeat until found or the search area is empty.
# - Step 4: If found, display its position; otherwise, print
#   "Mark Not Found."
#
# Time Complexity: O(n^2) for sorting + O(log n) for searching.

# Step 1: Sort the marks of 50 students in ascending order (Bubble Sort).
# Step 2: Ask the user to enter a mark.
# Step 3: Search that mark in the sorted list using Binary Search.
# Step 4: Show position if found, else show "Mark Not Found."

# sample marks of 50 students (values from 0 to 100)

marks = [56, 78, 90, 45, 67, 89, 34, 23, 99, 100,
         12, 67, 88, 45, 76, 90, 55, 43, 32, 21,
         65, 87, 98, 76, 54, 33, 22, 11, 44, 66,
         77, 88, 99, 60, 70, 80, 40, 50, 30, 20,
         10, 95, 85, 75, 65, 55, 45, 35, 25, 15]

# Step 1: Bubble Sort - ascending order
n = len(marks)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            temp = marks[j]
            marks[j] = marks[j + 1]
            marks[j + 1] = temp

print("Sorted Marks:", marks)

# Step 2: take mark from user
search_mark = int(input("\nEnter a mark to search: "))

# Step 3: Binary Search since the list is now sorted
low = 0
high = len(marks) - 1
found = False
position = -1

while low <= high:
    mid = (low + high) // 2

    if marks[mid] == search_mark:
        found = True
        position = mid
        break
    elif marks[mid] < search_mark:
        low = mid + 1
    else:
        high = mid - 1

# Step 4: display result
if found == True:
    print("Mark", search_mark, "found at position", position + 1)
else:
    print("Mark Not Found.")