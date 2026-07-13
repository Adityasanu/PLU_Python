'''2. Product ID Search
An e-commerce website stores product IDs in ascending order.
Write a program to find whether a customer-entered product ID exists in
the inventory. If it exists, display its index; otherwise, display "Product
Not Available."'''

    
# Approach:
# - The product IDs are already stored in ascending (sorted) order.
# - Because the list is sorted, we don't need to check every element
#   one by one - we can use Binary Search, which is much faster.
# - Binary Search works like this:
#     1. Look at the middle element of the list.
#     2. If it matches the ID we want, we are done.
#     3. If the middle element is smaller than the ID, the answer
#        must be in the right half, so we search there next.
#     4. If the middle element is bigger, the answer must be in
#        the left half, so we search there next.
#     5. Keep repeating this, cutting the list in half each time,
#        until we find the ID or run out of elements.
#
# Time Complexity: O(log n) - much faster than checking one by one.
 
# The list is already sorted in ascending order,
# so instead of checking one by one, we use Binary Search.
# It keeps cutting the list in half, so it is much faster.

product_ids = [101, 105, 110, 115, 120, 125, 130, 135, 140, 145]

search_id = int(input("Enter the Product ID to search: "))

low = 0
high = len(product_ids) - 1
found = False
position = -1

while low <= high:
    mid = (low + high) // 2

    if product_ids[mid] == search_id:
        found = True
        position = mid
        break
    elif product_ids[mid] < search_id:
        low = mid + 1          # search right half
    else:
        high = mid - 1         # search left half

if found == True:
    print("Product ID", search_id, "found at index", position)
else:
    print("Product Not Available.")