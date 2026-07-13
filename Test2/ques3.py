# Q3. Delete the node containing 30 from the linked list and display the updated list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
last = None
for v in [10, 20, 25, 30, 40, 50]:
    node = Node(v)
    if head is None:
        head = node
    else:
        last.next = node
    last = node

# find and delete the node with value 30
temp = head
prev = None
while temp is not None and temp.data != 30:
    prev = temp
    temp = temp.next

if temp is not None:
    if prev is None:
        head = temp.next
    else:
        prev.next = temp.next

# display the updated list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
print()