# Q1. Create a linked list containing the values 10, 20, 30, 40, 50 and display all the elements.

class Node:
    def __init__(self, value):
        self.value = value      
        self.next = None        


class LinkedList:
    def __init__(self):
        self.head = None       


    def add(self, value):
        new_node = Node(value)  

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next   

        current.next = new_node

    def display(self):
        current = self.head
        elements = []

        while current is not None:
            elements.append(str(current.value))
            current = current.next

        print(" -> ".join(elements))


my_list = LinkedList()

my_list.add(10)
my_list.add(20)
my_list.add(30)
my_list.add(40)
my_list.add(50)

my_list.display()