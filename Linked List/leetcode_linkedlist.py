"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Linked Lists  =========================================================
1. Leetcode 206. Reverse Linked List
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
2. Leetcode 876. Middle of the Linked List


"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Leetcode exercises
class Solution:
    # iteratives
    def reverseList_iter(self, head: ListNode) -> ListNode:
        pre = None
        current = head
        
        # loop through linked list
        while current:
            after = current.next
            current.next = pre
            pre = current
            current = after

        return pre

    # recursive
    def reverseList_recursive(self, head: ListNode) -> ListNode:
        current = head
        # base case 1 
        if current == None:
            return
        
        # base case 2
        if current.next == None:
            head = current
            return
        
        self.reverseList_recursive(current.next)

        # reverse part
        current.next.next = current
        current.next = None


    # Leetcode 876. Middle of the Linked List
    def middleNode(self, head: ListNode) -> ListNode:
        mid = head
        jumper = head

        while jumper and jumper.next:
            mid = mid.next
            jumper = jumper.next.next
        
        return mid



if __name__ == "__main__":
    



