''' 1. Student Roll Number Search
A teacher has stored the roll numbers of students in a list in the order
they registered. The list is not sorted.
Write a program to check whether a given roll number exists in the list.
If found, display its position; otherwise, print "Student Not Found." '''
    
   # Approach:
# The roll numbers are stored in the order students registered,
#   so the list is NOT sorted.
# Since it is unsorted, we cannot skip elements or guess a position,
#   we must check every roll number one by one from the start.
# This method is called Linear Search.
# We go through the list with a loop, compare each roll number
# with the one we are searching for.
# If it matches, we stop and note the position (found = True).
# If we reach the end without a match, the roll number does not exist.
#
# Time Complexity: O(n) - because in the worst case we check every element.
 
# The list is NOT sorted, so we check one by one from start to end.
# This is called Linear Search.

roll_numbers = [105, 101, 110, 107, 103, 109, 102, 108, 104, 106]

search_roll = int(input("Enter the roll number to search: "))

found = True
position = -1

for i in range(len(roll_numbers)):
    if roll_numbers[i] == search_roll:
        found = True
        position = i
        break   

if found == True:
    print("Roll number", search_roll, "found at position", position + 1)
else:
    print("Student Not Found.")