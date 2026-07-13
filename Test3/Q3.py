'''3. Arrange Exam Marks
A teacher wants to display students' marks from the lowest to the
highest.
Write a program to sort the marks of all students in ascending order.'''

'''Note
We use Bubble Sort: compare two neighbours, swap if
the left one is bigger than the right one.
Keep doing this until the whole list is sorted.'''

# Approach:
# - We need the marks arranged from lowest to highest.
# - We use Bubble Sort, which is the simplest sorting idea:
#     1. Compare two neighbouring marks.
#     2. If the left one is bigger than the right one, swap them
#        (because in ascending order, smaller should come first).
#     3. Move to the next pair and repeat.
#     4. After one full pass, the biggest mark "bubbles up" to the end.
#     5. Repeat the whole process for the remaining unsorted part,
#        one less element each time, until nothing needs swapping.
#
# Time Complexity: O(n^2) - fine for small lists like exam marks.

# We use Bubble Sort: compare two neighbours, swap if
# the left one is bigger than the right one.
# Keep doing this until the whole list is sorted.

marks = [67, 45, 89, 34, 90, 55, 78]

n = len(marks)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            # swap
            temp = marks[j]
            marks[j] = marks[j + 1]
            marks[j + 1] = temp

print("Marks in ascending order:", marks)