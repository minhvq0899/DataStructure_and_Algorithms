"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= 622. Design Circular Queue =========================================================
"""

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

"""
7 -> 

node = (7)
self.front = None
self.rear = None
self.currentSize = 0

"""
class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.front = None
        self.rear = None
        self.currentSize = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = Node(value)
        if self.isEmpty():
            self.front = node
        else:
            self.rear.next = node

        self.rear = node
        self.currentSize += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        temp = self.front
        self.front = self.front.next

        # In case both 'front' and 'rear' pointing to the same node, nullify 'rear' too
        if self.currentSize == 1:
            self.rear = None

        temp.next = None
        del temp
        self.currentSize -= 1

        return True

    def Front(self) -> int:
        if self.front:
            return self.front.value
        
        return -1

    def Rear(self) -> int:
        if self.rear:
            return self.rear.value
        
        return -1

    def isEmpty(self) -> bool:
        return self.currentSize == 0
        
    def isFull(self) -> bool:
        return self.currentSize == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()





