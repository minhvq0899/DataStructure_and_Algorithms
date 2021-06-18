"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Linked Lists =========================================================
Class Node
Class Linkedlist
    printList()
    placeOnTop(value)
    append(value)
    insert(targetNode, value)
    delete(value)

"""

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
    

class Linkedlist:
    def __init__(self):
        self.head = None

    # Prints all elements in Linked List
    def printList(self): 
        current = self.head 
        while (current): 
            print(current.val) 
            current = current.next

    # Put an element at the beginning of a Linked List
    def placeOnTop(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    # Put an element at the end of a Linked List
    def append(self, value):
        node = Node(value)
        
        if not self.head:
            self.head = node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    # Insert a node after a known node
    def insert(self, targetNode, value):
        node = Node(value)
        node.next = targetNode.next
        targetNode.next = node

    # Delete a node
    def delete(self, value):
        current = self.head
        # check if it's the head node
        if value == current.val:
            self.head = current.next
            current = None
            return
        
        # loop through
        pre = None
        while current:
            # found the wanted node
            if current.val == value:
                break
            pre = current
            current = current.next
        
        pre.next = current.next
        current = None

