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
4. Leetcode 234. Palindrome Linked List
5. Leetcode 21. Merge Two Sorted Listss
6. Leetcode 445. Add Two Numbers II
7. Leetcode 1836. Remove Duplicates From an Unsorted Linked List 
=========================================================
Leetcode template:
8. Leetcode 19. Remove Nth Node From End of List
9. Leetcode 24. Swap Nodes in Pairs
10. Leetcode 86. Partition List
11. Leetcode 141 + 142. Linked List Cycle
12. Leetcode 237. Delete Node in a Linked List
13. Leetcode 2. Add Two Numbers

"""
from linkedlist import * 
from typing import List


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Leetcode exercises
class Solution:
    # Leetcode 206. Reverse Linked List
    # iteratives
    def reverseList_iter(self, head: ListNode) -> ListNode:
        # ======== Step 2 ========
        current = head
        prev = None

        while current:
            after = current.next
            current.next = prev
            prev = current
            current = after

        return prev


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
    

    # ----------------------------------------------------------------------------------------------------------

    # Leetcode 876. Middle of the Linked List
    def middleNode(self, head: ListNode) -> ListNode:
        mid = head
        jumper = head

        while jumper and jumper.next:
            mid = mid.next
            jumper = jumper.next.next
        
        return mid

    # ----------------------------------------------------------------------------------------------------------

    # Leetcode 160. Intersection of Two Linked Lists
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # ===== Step 1 =====
        # Set dummy: this problem does not require dummy
        
        # ===== Step 2 =====
        pA = headA
        pB = headB
        
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB
            
            if pB:
                pB = pB.next
            else:
                pB = headA
        
        # Even if the two list do not intersect, pA and pB will reach the end of 
        # two lists at the same time -> they will both be None at the same time
        
        # ===== Step 3 =====
        return pA       # or pB because now pA == pB
            

    # ----------------------------------------------------------------------------------------------------------

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

    # ----------------------------------------------------------------------------------------------------------

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

    # ----------------------------------------------------------------------------------------------------------
    
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


    # ----------------------------------------------------------------------------------------------------------
        
    # Leetcode 1836. Write code to remove duplicates from an unsorted linked list.
    # FOLLOW UP
    # How would you solve this problem if a temporary buffer is not allowed? 
    def deleteDups(self, head: ListNode) -> ListNode:
        prev = head
        h = head.next
        dups = set()
        dups.add(head.val)

        while h: 
            if h.val in dups: 
                prev.next = h.next
            else:
                dups.add(h.val)
                prev = prev.next
            
            h = h.next
        
        return head

    # ===================================================================================================
    # Leetcode template:         
    # Leetcode 19. Remove Nth Node From End of List
    # Given the head of a linked list, remove the nth node from the end of the list and return its head.
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # ========== Step 1: Set up dummy node ========== 
        dummy = ListNode(0, head)
        
        # ========== Step 2: we move our walker/ runner in a loop ========== 
        # use two pointers
        walker = dummy
        runner = dummy

        # set up runner to be n steps ahead of walker
        for k in range (n):
            runner = runner.next

        # bring runner to the end node
        while runner and runner.next != None:
            walker = walker.next
            runner = runner.next

        # remove the Nth from the end
        walker.next = walker.next.next
            
        # ========== Step 3: Recover the head via dummy ========== 
        return dummy.next

    # ---------------------------------------------------------------

    # Leetcode 24. Swap Nodes in Pairs
    def swapPairs(self, head: ListNode) -> ListNode:
        # ========= Step 1: Set up dummy node =========
        dummy = ListNode(0, head)
        
        # ========= Step 2: Move our walker/ runner =========
        walker = dummy
        runner = dummy
        while walker.next and walker.next.next:         # while there are at least two more nodes
            runner = runner.next
            # three steps to swap nodes in pair
            walker.next = walker.next.next
            runner.next = runner.next.next
            walker.next.next = runner
            
            # update runner and walker
            walker = walker.next.next
        
        # ========= Step 3: Recover the head via dummy =========
        return dummy.next

    # ---------------------------------------------------------------

    # Leetcode 86. Partition List
    # Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
    # You should preserve the original relative order of the nodes in each of the two partitions.
    def partition(self, head: ListNode, x: int) -> ListNode:
        # =========== Step 1 ===========
        dummy_less = ListNode()
        dummy_more = ListNode()
        
        # =========== Step 2 ===========
        walker_less = dummy_less
        walker_more = dummy_more
        while head:
            if head.val < x:
                walker_less.next = head
                walker_less = walker_less.next
            else:
                walker_more.next = head
                walker_more = walker_more.next
            
            head = head.next
        
        # merge the new "more" list to the end of "less" list
        walker_less.next = dummy_more.next
        walker_more.next = None

        # =========== Step 3 ===========
        return dummy_less.next
    

    # ---------------------------------------------------------------

    # Leetcode 141 + 142. Linked List Cycle
    # 141. Dectect a cycle
    # Idea 1: We can use a HashSet, this solution may take O(n) memory
    # Idea 2: We can use Floy's Cycle detection 
    def hasCycle(self, head: ListNode) -> bool:
        # =========== Step 2: Move our walker and runner ===========
        walker = head;         
        runner = head; 
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next

            if walker == runner: return True
            
        return False


    def detectCycle(self, head: ListNode) -> ListNode:
        hasCycle = False
        # =========== Step 2: Move our walker and runner ===========
        walker = head;         
        runner = head; 
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next

            if walker == runner: 
                hasCycle = True
                break
            
        # Find where the cycle starts
        if not hasCycle:
            return None
        else:
            walker = head
            # move both walker and runner one step at a time
            while walker != runner: 
                walker = walker.next
                runner = runner.next
            return walker


    # ---------------------------------------------------------------
    # Leetcode 237. Delete Node in a Linked List
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        runner = node.next
        node.val = runner.val
        node.next = runner.next
        

    # ---------------------------------------------------------------
    # Leetcode 2. Add Two Numbers
    """
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    # Idea: compute the sum and store it in an integer, then create a new linked list to store the result
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # ========== Step 1 ==========
        dummy = ListNode()
        walker = dummy

        # ========== Step 2 ==========
        # compute the value stored in l1 and l2
            # for l1
        count = 0
        l1_int = 0
        walker_l1 = l1; 
        while walker_l1:
            l1_int += walker_l1.val* (10**count)
            count += 1
            walker_l1 = walker_l1.next

            # for l2
        count = 0
        l2_int = 0
        walker_l2 = l2; 
        while walker_l2:
            l2_int += walker_l2.val* (10**count)
            count += 1
            walker_l2 = walker_l2.next
        
        # store the sum in l1_int
        l1_int += l2_int
        if l1_int == 0: return dummy    # special case

        # now create a new list to store
        while l1_int:
            remainder = l1_int % 10
            l1_int = l1_int // 10
            node = ListNode(remainder)
            walker.next = node
            walker = walker.next

        # ========== Step 3 ==========
        return dummy.next

        







if __name__ == "__main__":
    hanoi = Node('Ha Noi')
    quangbinh = Node('Quang Binh')
    quangbinh2 = Node('Quang Binh')
    danang = Node('Da Nang')
    saigon = Node('Sai Gon')
    saigon2 = Node('Sai Gon')

    hanoi.next = quangbinh
    quangbinh.next = quangbinh2
    quangbinh2.next = danang
    danang.next = saigon
    saigon.next = saigon2

    linkedlist_obj = Linkedlist()
    linkedlist_obj.head = hanoi; 
    linkedlist_obj.printList()
    # Ha Noi -> Quang Binh -> Quang Binh -> Da Nang ->  Sai Gon -> Sai Gon

    solution = Solution()
    linkedlist_obj.head = solution.deleteDups(linkedlist_obj.head)
    linkedlist_obj.printList()





