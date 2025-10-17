"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Linked Lists  =========================================================
Template for sublist reversal
Template to merge two SEPARATE LinkedLists

(Easy)
Leetcode 206. Reverse Linked List
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
(Medium version) Leetcode 92. Reverse Linked List II - Template for sublist reversal
Leetcode 876. Middle of the Linked List
Leetcode 160. Intersection of Two Linked Lists
Leetcode 234. Palindrome Linked List
Leetcode 21. Merge Two Sorted Lists
Leetcode 203. Remove Linked List Elements

(Medium)
Leetcode 445. Add Two Numbers II
Leetcode 1836. Remove Duplicates From an Unsorted Linked List 
Leetcode 19. Remove Nth Node From End of List
Leetcode 24. Swap Nodes in Pairs
Leetcode 86. Partition List
Leetcode 141 + 142. Linked List Cycle
Leetcode 237. Delete Node in a Linked List
Leetcode 2. Add Two Numbers
Leetcode 138. Copy List with Random Pointer
Leetcode 430. Flatten a Multilevel Doubly Linked List
Leetcode 61. Rotate List
Leetcode 143. Reorder List 
    - Template for sublist reversal
    - Template to merge two SEPARATE LinkedLists
Leetcode 328. Odd Even Linked List

(Hard)
Leetcode 23. Merge k Sorted Lists
Leetcode 25. Reverse Nodes in k-Group - Template for sublist reversal

"""
from linkedlist import * 
from typing import List
import heapq
import Optional
from collections import defaultdict


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node138:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Node430:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Leetcode exercises
class Solution:
    # This helper fn helps print a LinkedList
    def printLinkedList(self, head: ListNode): 
        current = head 
        while (current): 
            print("%d ->" % (current.val), end=" ") 
            current = current.next

        print("\n")

    # This helper fn is to prepare a head Node for input param
    def prepareInput(self, nums: List[int]) -> ListNode:
        head = ListNode(nums[0])
        current = head

        for i in range (1, len(nums)):
            node = ListNode(nums[i])
            current.next = node
            current = current.next
        
        return head

    # Template for sublist reversal
    def reverseBetween(head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move prev to node before reversal starts
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse sublist
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
    
    # Template to merge two SEPARATE LinkedLists
    # 'first' and 'second' are the two heads of the two lists
        # tmp1 saves the next node in the first half
        # tmp2 saves the next node in the second half
        # You interleave: first → second → tmp1 → tmp2 → ...
        # Stops when either half runs out
    def merge_halves(first, second):
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            if not tmp1:
                break
            second.next = tmp1

            first = tmp1
            second = tmp2
    
    # ----------------------------------------------------------------------------------------------------------
    # Leetcode 206. Reverse Linked List
    # iteratives
    def reverseList_iter(self, head: ListNode) -> ListNode:
        """
        # ======== Step 2 ========
        current = head
        prev = None

        while current:
            after = current.next
            current.next = prev
            prev = current
            current = after

        return prev
        """
        prev = ListNode()

        while head:
            self.printLinkedList(head)
            after = head.next
            head.next = prev
            after.next = head
            prev = head
            head = after

        self.printLinkedList(prev)
        return prev

    # recursive
    """
    rL(1)
    current = 0
    h = rl(1)
        current = 1
        h = rl(2)
            current = 2
            h = rl(3) -> return 3
            3.next = 2
            2.next = None
            return 3
        2.next = 1
        1.next = None
        return 3
    ...
    return 3
    """
    def reverseList_recursive(self, head: ListNode) -> ListNode:
        # Step 1: Base case 
        if head == None:
            return None
        if head.next == None:
            return head
        
        current = head
        
        # Step 2: DFS part -> build solution bottome up
        h = self.reverseList_recursive(current.next)

        # Step 3: Action - reverse part
        current.next.next = current
        current.next = None

        # Step 4: return
        return h

    # ----------------------------------------------------------------------------------------------------------
    # Leetcode 92. Reverse Linked List II
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move prev to node before reversal starts
        for _ in range(left - 1):
            prev = prev.next

        # Iteratively reverse sublist
        current = prev.next             # start at leftNode
        for _ in range(right-left):
            after = current.next
            current.next = after.next
            after.next = prev.next
            prev.next = after

        return dummy.next

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
    # Leetcode 203. Remove Linked List Elements
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Step 1: Create dummy node
        dummy = ListNode(None, None)
        dummy.next = head

        # Step 2: Traverse with curr
        curr = dummy
        while curr.next:
            # Skipping the next node (curr.next)
            if curr.next.val == val:
                # Notice: here we are only updating 'curr.next', not 'curr'
                curr.next = curr.next.next
            else:
                # Move curr up
                curr = curr.next

        return dummy.next

    # ==========================================================================================================
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
                prev.next = h.next  # skip h
            else:
                dups.add(h.val)
                prev = prev.next
            
            h = h.next
        
        return head
     
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
        walker = head         
        runner = head
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next

            if walker == runner: return True
            
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        hasCycle = False
        # =========== Step 2: Move our walker and runner ===========
        walker = head         
        runner = head
        
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

    # ---------------------------------------------------------------    
    # Leetcode 138. Copy List with Random Pointer
    def copyRandomList(self, head: 'Node138') -> 'Node138':
        if not head:
            return None

        # Pass 1: Make a copy for each node and insert it right after the original
        curr = head
        while curr:
            copy = Node138(curr.val, curr.next, curr.random)
            curr.next = copy
            curr = copy.next

        # Pass 2
        # Assign the right random pointers to the copied nodes
        # Separate the original and copied lists 
        copy_head = head.next
        curr = copy_head
        while curr:
            if curr.next:
                curr.next = curr.next.next
            if curr.random:
                curr.random = curr.random.next
            curr = curr.next

        return copy_head

    # ---------------------------------------------------------------    
    # Leetcode 430. Flatten a Multilevel Doubly Linked List
    def flatten(self, head: Node430) -> Node430:
        if not head: return None
        self.dfs(head)

        return head

    # This fn will always return the tail of the flatten list
    def dfs(self, head):
        # Track 'current' and tail of the flatten list
        current = head
        tail = head

        # Todo: loop through current
        while current:
            nextNode = current.next
            # If there is a child, flatten it first
            if current.child:
                childHead = current.child
                childTail = self.dfs(childHead)

                # Insert the child node flattened between current and last of next_node
                current.next = childHead
                childHead.prev = current

                # Connect child tail to next_node if next_node exists
                if nextNode:
                    childTail.next = nextNode
                    nextNode.prev = childTail

                # Nullify the child pointer
                current.child = None
                tail = childTail
            else:
                tail = current

            current = nextNode

        # Return the tail of the flatten list
        return tail

    # ---------------------------------------------------------------    
    # Leetcode 61. Rotate List
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        llLen = 0
        current = head
        while current:
            current = current.next
            llLen += 1

        # print(llLen)

        k = k % llLen
        if k == 0:
            return head

        # currentPlusK will be k nodes after current
        # We will keep track of currentPlustKPrev, which will be (k-1) nodes after current
        current = head
        currentPlusKPrev = current
        for _ in range(k-1):
            if currentPlusKPrev.next:
                currentPlusKPrev = currentPlusKPrev.next
            else:
                break

        # Move currentPlusKPrev to the tail node of the LL
        currentPrev = None
        while currentPlusKPrev.next:
            currentPrev = current
            current = current.next
            currentPlusKPrev = currentPlusKPrev.next

        # Update next pointer
        currentPlusKPrev.next = head
        if currentPrev:
            currentPrev.next = None

        return current

    # Leetcode 143. Reorder List
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev = None
        walker = runner = head

        # walker will be the mid point of our LL
        while runner and runner.next:
            prev = walker
            walker = walker.next
            runner = runner.next.next

        # corner case where LL has len 1
        if not prev: 
            return
        
        # Reverse the second half of LL
        while walker.next:
            after = walker.next
            walker.next = after.next
            after.next = prev.next
            prev.next = after

        # First half will be 'head' to 'prev'
        # Second half will be prev.next to the end
        # IMPORTANT: it has two be two separate list for the merging template below to work
        first, second = head, prev.next
        prev.next = None    # separate two lists

        # tmp1 saves the next node in the first half
        # tmp2 saves the next node in the second half
        # You interleave: first → second → tmp1 → tmp2 → ...
        # Stops when either half runs out
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            if not tmp1:
                break
            second.next = tmp1

            first = tmp1
            second = tmp2

    # Leetcode 328. Odd Even Linked List
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        currentOdd = head
        currentEven = head.next
        headEven = head.next
        while currentEven and currentEven.next:
            # Connect
            currentOdd.next = currentEven.next
            currentOdd = currentOdd.next

            currentEven.next = currentOdd.next
            currentEven = currentEven.next

        # Connect two LL
        currentOdd.next = headEven

        return head

            
             







    # ===============================================================
    # ---------------------------------------------------------------    
    # Leetcode 23. Merge k Sorted Lists
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # if not lists: return []
        # ----------------------------------------------
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        # ----------------------------------------------
        # create a heap and add all heads 
        heap = []
        for node in lists:      # O(n)
            if node:
                heapq.heappush(heap, Wrapper(node))

        dummy = ListNode()      # to keep track of the head
        current = dummy
        # keep popping the heap 
        while len(heap) != 0:
            node = heapq.heappop(heap).node
            current.next = node
            current = current.next
            # if node is not the last node in its list, add node.next to the heap
            # this way the heap will always have size of n, with n is the number of LinkedLists
            if node and node.next: heapq.heappush(heap, Wrapper(node.next))

        return dummy.next

    # Follow-up: Merge in-place
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Refer back to our 'lists' variable for all the heads
        # Dict: value -> index of head in 'lists'
        '''
        lists = [ 2, 3]
        valueToIndexHead = {1:[node1, node2]}

        '''
        valueToIndexHead = defaultdict(list)
        heap = []
        for i, head in enumerate(lists):
            if head:
                heap.append((head.val, i)) # Add value to heap

        # Merge in place
        heapq.heapify(heap)
        current = ListNode()
        head = current
        while heap:
            val, i = heapq.heappop(heap)           # a value
            current.next = lists[i]
            current = current.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        return head.next

    # Leetcode 25. Reverse Nodes in k-Group
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        kMinusOneNodesAfterCurrent = current        # A spy that travel ahead to see if we need to visit the next partition
        for _ in range(k-1):
            if kMinusOneNodesAfterCurrent:
                kMinusOneNodesAfterCurrent = kMinusOneNodesAfterCurrent.next

        while kMinusOneNodesAfterCurrent:
            # Reverse the next k nodes, following the template
            for _ in range(k-1):
                after = current.next
                current.next = after.next
                after.next = prev.next
                prev.next = after

            prev = current
            current = prev.next

            # Send a spy (k-1) nodes ahead
            kMinusOneNodesAfterCurrent = current
            for _ in range(k-1):
                if kMinusOneNodesAfterCurrent:
                    kMinusOneNodesAfterCurrent = kMinusOneNodesAfterCurrent.next

        return dummy.next


        



















if __name__ == "__main__":
    """
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
    """

    solution = Solution()

    # Prepare input parameter
    nums = [1,2,3,4,5]
    head = solution.prepareInput(nums)
    # solution.printLinkedList(head)
    solution.reverseList_iter(head)


    






