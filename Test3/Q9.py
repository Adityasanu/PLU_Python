'''9. Library Book Search
A library has 10,000 books, and the Book IDs are already arranged in
ascending order.
Write a program to find a given Book ID efficiently.
Also mention which searching algorithm you used and why it is suitable.'''

# Approach:
# - There are 10,000 books, and their Book IDs are already
#   arranged in ascending (sorted) order.
# - Because the list is sorted, we don't need to check every
#   book one by one - we can use Binary Search:
#     1. Look at the middle Book ID.
#     2. If it matches what we searched for, we are done.
#     3. If the middle ID is smaller than the target, the book
#        must be in the right half, so search there next.
#     4. If the middle ID is bigger, the book must be in the
#        left half, so search there next.
#     5. Keep repeating, cutting the search area in half each
#        time, until the book is found or the search area is empty.
#
# Why Binary Search is suitable here:
# - Linear search would take up to 10,000 steps in the worst case.
# - Binary Search cuts the search area in half every time,
#   so it only takes about log2(10000) = 14 steps in the worst case.
# - This works only because the list is already sorted.
 
# creating a sample sorted list of 10,000 book IDs (1 to 10000)

book_ids = list(range(1, 10001))

search_id = int(input("Enter the Book ID to search: "))

low = 0
high = len(book_ids) - 1
found = False
position = -1

while low <= high:
    mid = (low + high) // 2

    if book_ids[mid] == search_id:
        found = True
        position = mid
        break
    elif book_ids[mid] < search_id:
        low = mid + 1
    else:
        high = mid - 1

if found == True:
    print("Book ID", search_id, "found at index", position)
else:
    print("Book Not Found.")

print("Algorithm Used: Binary Search (because the list is already sorted)")