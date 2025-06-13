"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Implement Queue/Stack using Stacks/Queues =========================================================

Leetcode 232. Implement Queue using Stacks
Leetcode 225. Implement Stack using Queues

"""

from typing import List
from queue import Queue

"""
Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
"""
# Leetcode 232. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                pop1 = self.stack1.pop()
                self.stack2.append(pop1)

        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2: return self.stack2[ len(self.stack2)-1 ]
        elif self.stack1: return self.stack1[0]
        else: return None

    def empty(self) -> bool:
        return not ( len(self.stack1) > 0 or len(self.stack2) > 0 )




"""
Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
"""
# Leetcode 225. Implement Stack using Queues
class MyStack:
    def __init__(self):
        self.q1 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)
        for _ in range ( self.q1.qsize()-1 ):
            self.q1.put( self.q1.get() )

    def pop(self) -> int:
        return self.q1.get()
        
    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()
        






if __name__ == "__main__":
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    print(obj.top())
    print(obj.pop())
    print(obj.empty())













