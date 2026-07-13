'''6. Employee Salary Report
An HR department has employee salary records collected from two different
branches.
Write a program to combine both lists and display all salaries in
ascending order.'''

# Approach:
# - We are given two separate salary lists, one from each branch.
# - Step 1: Combine (merge) both lists into a single list using +,
#   so all salaries are together in one place.
# - Step 2: Since the combined list is not sorted, we sort it using
#   Bubble Sort:
#     1. Compare neighbouring salaries.
#     2. Swap if the left one is bigger than the right one.
#     3. Repeat until the whole list is in ascending order.
# - The final result is one combined, sorted salary report.
#
# Time Complexity: O(n^2) for sorting, O(n) for combining.

# We have salary lists from two branches.
# Step 1: Combine both lists into one.
# Step 2: Sort the combined list in ascending order using Bubble Sort.

branch1_salaries = [35000, 42000, 28000, 51000]
branch2_salaries = [39000, 47000, 31000, 55000, 26000]

# combine both lists
all_salaries = branch1_salaries + branch2_salaries

n = len(all_salaries)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if all_salaries[j] > all_salaries[j + 1]:
            temp = all_salaries[j]
            all_salaries[j] = all_salaries[j + 1]
            all_salaries[j + 1] = temp

print("All Salaries (Ascending Order):", all_salaries)