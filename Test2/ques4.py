# Q4. Count and display the total number of nodes in the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
last = None
for v in [10, 20, 25, 40, 50]:
    node = Node(v)
    if head is None:
        head = node
    else:
        last.next = node
    last = node

# count the number of nodes
count = 0
temp = head
while temp is not None:
    count += 1
    temp = temp.next

print("Total nodes:", count)