"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Doubly Linked Lists =========================================================
Class Node
Class DoublyLinkedList
    __init__(key, value)
    insert_head(key, value)
    delete_tail()
    move_to_head(key)
    print_list()

"""

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, key: int, value: int):
        new_node = Node(key, value)
        if not self.head:  # Empty list case
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_tail(self):
        if not self.tail:  # Empty list
            return
        if self.head == self.tail:  # Single node case
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def move_to_head(self, key: int):
        if not self.head:
            return
        current = self.head
        while current and current.key != key:
            current = current.next
        
        if not current or current == self.head:  # Node not found or already head
            return
        
        # If tail is being moved, update tail reference
        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
        
        # Detach current node
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        
        # Move node to head
        current.prev = None
        current.next = self.head
        self.head.prev = current
        self.head = current

    def print_list(self):
        current = self.head
        while current:
            print(f"({current.key}, {current.value})", end=" <-> ")
            current = current.next
        print("None")








if __name__ == "__main__":
    # Example Usage
    dll = DoublyLinkedList()
    dll.insert_head(1, 100)
    dll.insert_head(2, 200)
    dll.insert_head(3, 300)
    dll.print_list()  # Output: (3, 300) <-> (2, 200) <-> (1, 100) <-> None

    dll.delete_tail()
    dll.print_list()  # Output: (3, 300) <-> (2, 200) <-> None

    dll.move_to_head(2)
    dll.print_list()  # Output: (2, 200) <-> (3, 300) <-> None