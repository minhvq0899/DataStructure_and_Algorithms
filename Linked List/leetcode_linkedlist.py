"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Linked Lists  =========================================================
1. Leetcode 206. Reverse Linked List
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
2. Leetcode 876. Middle of the Linked List
3. Leetcode 160. Intersection of Two Linked Lists
4. Leetcode 24. Swap Nodes in Pairs
5. Leetcode 234. Palindrome Linked List
6. Leetcode 21. Merge Two Sorted Listss
7. Leetcode 445. Add Two Numbers II

"""

from typing import List


# Definition for singly-linked list
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


    # Leetcode 160. Intersection of Two Linked Lists
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # use two pointers: a and b
        # when a traverses and reaches the end of A, redirect it to head of B   
        # the same for b
        a = headA
        b = headB
        
        if a == None or b == None:
            return None
        
        # if headA and headB do have intersections, their last node must be the same
        lastA = None
        lastB = None
        # check if a or b has finish both traverse
        switchA = False
        switchB = False
        while a != b:
            if a.next != None: 
                a = a.next
            else: 
                if not switchA: 
                    switchA = True
                    lastA = a
                    a = headB
                else: 
                    break

            if b.next != None: 
                b = b.next
            else:
                if not switchB:
                    switchB = True
                    lastB = b
                    b = headA
                else:
                    break
                
        if lastA != lastB: 
            return None
        else:
            return a



    # Leetcode 24. Swap Nodes in Pairs
    def swapPairs(self, head: ListNode) -> ListNode:
        # make sure the LL is at least 2 Node long
        if head == None or head.next == None:
            return head
        
        # set beginning node
        pre = ListNode(None, head)
        
        current = head
        final_head = current.next
        after = current # this will be our anchor
        
        while after and after.next:
            # connect the previous two with the following two
            pre.next = after.next
            
            # use after as an anchor to set pre and current 
            pre = after
            current = after.next
            
            # swaping part 
            pre.next = current.next
            current.next = pre
            
            # reset our anchor
            after = pre.next
                
        return final_head


    # Leetcode 234. Palindrome Linked List
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        
        current = head
        jump = head
        
        while jump.next and jump.next.next: # O(n)
            current = current.next
            jump = jump.next.next
        
        # check to see if the length of LL is odd or even: O(n)
        if jump.next: # even
            half = self.reverseList(current.next)
        else: # odd
            half = self.reverseList(current)
        
        # if you want to seperate two halves:
        # current.next = None
        
        # check palindrome
        while half: # O(n)
            if head.val != half.val:
                return False
            head = head.next
            half = half.next
        
        return True


    # Leetcode 21. Merge Two Sorted Lists
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # in case one the the two list is empty
        if not l1: return l2
        elif not l2: return l1
        
        # set head
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        anchor = head
            
        # loop
        while l1 and l2:
            if l1.val < l2.val:
                anchor.next = l1
                l1 = l1.next
                anchor = anchor.next
            else: 
                anchor.next = l2
                l2 = l2.next
                anchor = anchor.next
        
        # connect the final list with the rest of l1 or l2
        if l1: anchor.next = l1
        elif l2: anchor.next = l2
        
        return head

    
    # Leetcode 445. Add Two Numbers II
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # turn l1 and l2 into int: O(n)
        n1 = 0
        while l1:
            n1 = (n1 * 10) + l1.val
            l1 = l1.next
        
        n2 = 0
        while l2:
            n2 = (n2 * 10) + l2.val
            l2 = l2.next
        
        n3 = n1 + n2
        
        # turn n3 into LinkedList: O(n)
        val = n3 % 10
        n3 = n3 // 10
        head3 = ListNode(val, None)
        
        while n3:
            val = n3 % 10
            n3 = n3 // 10
            newnode = ListNode(val, head3)
            head3 = newnode
            
        return head3
        
        
    

if __name__ == "__main__":
    n3 = 7 // 10
    print(n3)



