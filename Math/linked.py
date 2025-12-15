class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, value, pos):
        new_node = Node(value)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return 
        temp = self.head
        current = 1
        while temp.next is not None and current < pos-1:
            temp = temp.next
            current += 1
        if temp is None:
            print("Position out of range")
            return 
        new_node.next = temp.next
        temp.next
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print("None")
l = LinkedList()
l.insert_at_end(10)
l.insert_at_end(20)
l.insert_at_end(30)
l.display()
