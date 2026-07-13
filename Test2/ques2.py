# Q2. Insert a new node containing 25 after the node containing 20.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None # this is the
last = None
for v in [10, 20, 30, 40, 50]: #this is 
    node = Node(v)
    if head is None:
        head = node
    else:
        last.next = node
    last = node

temp = head
while temp is not None:
    if temp.data == 20:
        new_node = Node(25)
        new_node.next = temp.next
        temp.next = new_node
        break
    temp = temp.next

temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
print()
    