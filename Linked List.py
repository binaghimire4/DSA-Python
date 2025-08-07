#A linked list is a lijear data structure that stores elements in a sequence but arrays.
#like array but it doesnt need contiguous memory locations. It is made of connected nodes, each containing data a reference to the next node in the squence#

class Node:
    def __init__(self, data):
        self.data = data
        self. next = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(13)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=' ')
    currentNode = currentNode.next
print('Null')

#Doubly Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(3)
node2 = Node(22)
node3 = Node(10)
node4 = Node(16)

node1.next = node2
node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("\n Traversing forward:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" ")
    currentNode = currentNode.next
print("null")

print("\nTraversing backward:")
currentNode = node4
while currentNode:
    print(currentNode.data, end=" ")
    currentNode = currentNode.prev
print("Null")



