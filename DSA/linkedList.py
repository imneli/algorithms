class Node:
    def __init__(self, data):
        self.data = data # value stored in the node
        self.next = None  # pointer for the next node

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data) # create a new node in the end of the array 
        if self.head is None:
            self.head = new_node # the new node becomes the first
            return
        last_node = self.head
        while last_node.next: # at the last node
            last_node = last_node.next
        last_node.next = new_node 

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("none")

arr = LinkedList()

arr.append(10)
arr.append(20)
arr.append(30)

arr.print_list()
