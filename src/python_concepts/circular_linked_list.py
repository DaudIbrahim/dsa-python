# Loop a Circular Linked List without running into an infinite loop


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def traverse(self):
        if not self.head:
            return

        current = self.head

        while True:
            current = current.next
            print(current.data)

            if current == self.head:
                break


# Usage:
# Create a circular linked list
clist = CircularLinkedList()
clist.insert(1)
clist.insert(2)
clist.insert(3)
clist.insert(4)
clist.insert(5)

# Traverse the list
clist.traverse()

# Expected Outputer
# 1 2 3 4 5
