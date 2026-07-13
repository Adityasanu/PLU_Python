'''8. Hospital Emergency Queue
A hospital has a list of patients with different priority levels.
Write a program to arrange the patients so that the patient with the
highest priority is treated first.'''

# Approach:
# - Each patient has a name and a priority number.
# - A higher priority number means a more serious condition,
#   so that patient must be treated FIRST.
# - This means we need to sort patients by priority in
#   descending order (highest priority first).
# - We store each patient as a pair [name, priority] inside a list,
#   so both values move together when we sort.
# - We use Bubble Sort on the priority value:
#     1. Compare the priority of two neighbouring patients.
#     2. Swap their entire [name, priority] pair if the left
#        patient's priority is smaller than the right one's.
#     3. Repeat until patients are arranged from highest to
#        lowest priority.
# - Finally, we print the patients in this treatment order.
#
# Time Complexity: O(n^2)
 
# Each patient has a name and a priority number.
# Higher priority number = more serious condition = treated first.
# We sort the patients by priority in descending order.
 
# storing each patient as [name, priority]

patients = [
    ["Amit", 3],
    ["Sara", 5],
    ["Rahul", 1],
    ["Neha", 4],
    ["Vikram", 2]
]

n = len(patients)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if patients[j][1] < patients[j + 1][1]:
            temp = patients[j]
            patients[j] = patients[j + 1]
            patients[j + 1] = temp

print("Treatment Order (Highest Priority First):")
turn = 1
for patient in patients:
    print(turn, "-", patient[0], "(Priority:", patient[1], ")")
    turn = turn + 1