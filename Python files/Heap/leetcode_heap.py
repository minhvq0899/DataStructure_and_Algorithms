"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Heap  =========================================================
(Easy)
Leetcode 1337. The K Weakest Rows in a Matrix

(Medium)
Leetcode 451. Sort Characters By Frequency
Leetcode 215. Kth Largest Element in an Array
Leetcode 767. Reorganize String
Leetcode 378. Kth Smallest Element in a Sorted Matrix
Leetcode 373. Find K Pairs with Smallest Sums
Template: 
Leetcode 347. Top K Frequent Elements
Leetcode 23. Merge k Sorted Lists
Leetcode 973. K Closest Points to Origin
Leetcode 659. Split Array into Consecutive Subsequences
Leetcode 692. Top K Frequent Words
Leetcode 621. Task Scheduler

(Hard)
Leetcode 295. Find Median from Data Stream 

"""

from typing import List, Optional
import heapq 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Why is it important that the max heap will always have equal or more element than min heap?
1. Median Calculation Depends on Heap Sizes
    - If both heaps are the same size → Median is the average of the two roots.
    - If bottom_heap has one more element → Median is the root of bottom_heap.
    Maintaining this structure simplifies findMedian() logic to just check sizes and access the root(s).
2. Correctly Reflects Value Distribution
    - All values in bottom_heap must be ≤ all values in top_heap.
    - Keeping the larger half slightly smaller ensures the lower half stays dominant when total count is odd, so the true median lies in the max heap.
3. Efficient Updates
    - Inserting a new value and rebalancing lets us avoid sorting the entire data stream.
    - Each addNum() takes O(log n) time thanks to the reheap operations.

"""
# Leetcode 295. Find Median from Data Stream
class MedianFinder:
    def __init__(self):
        self.top_heap = []          # a min heap of upper half
        self.bottom_heap = []       # a max heap of bottom half
    
    def addNum(self, num: int) -> None:
        # we will set up in the way that the max heap will always have equal or more element than min heap
        heapq.heappush(self.bottom_heap, (-1)*num)
        popBottom = heapq.heappop(self.bottom_heap)
        heapq.heappush(self.top_heap, (-1)*popBottom)

        # maintain the right size for two heaps
        if len(self.bottom_heap) < len(self.top_heap):
            heapq.heappush( self.bottom_heap, (-1)*heapq.heappop(self.top_heap) )

    def findMedian(self) -> float:
        if len(self.bottom_heap) == len(self.top_heap):
            return ( (-1)*self.bottom_heap[0] + self.top_heap[0] ) / 2
        else:   # max heap has more element
            return self.bottom_heap[0] * (-1)



class Solution:
    # Leetcode 1337. The K Weakest Rows in a Matrix
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []  
        # -----------------
        # row = [1,1]
        # binarySearch có 2 dạng:
        # 1. Find the exact index of some number
        # 2. Find the first or last index of some number
        # This is second case
        def binarySearch(row: List[int]) -> int:
            left, right = 0, len(row)-1
            result = 0

            while left <= right:
                mid = (left+right)//2
                if row[mid] == 0:
                    right = mid -1
                else:
                    result = mid + 1
                    left = mid + 1

            return result
        # -----------------
        for r in range(len(mat)):
            numberOfSolider = binarySearch(mat[r])
            heap.append((numberOfSolider, r))

        heapq.heapify(heap)

        result = []
        for _ in range(k):
            pop = heapq.heappop(heap)
            result.append(pop[1])

        return result

    # ================================================================================
    # Leetcode 451. Sort Characters By Frequency
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = []       # Use max-heap
        
        for char, freq in counter.items():
            heap.append( (-freq, char) )
        
        heapq.heapify(heap)

        result = []

        '''
        s = 'aabcd'
        heap = [(-2, a)]
        pop = (-2, a), heap = []
        result = a
        
        Input: s = "tree"
        Output: "eert"
        '''

        '''
        a = m characters
        b = n characters

        a += b -> time ??

        '''
        # If the char has freq of more than 1, then we need to pop them in order
        while heap and heap[0][0] < -1:
            pop = heapq.heappop(heap)
            result.append(pop[1] * -pop[0])

        # The rest of the heap are chars with freq of 1 -> doesn't matter the order
        for _, char in heap:
            result.append(char)

        return ''.join(result)

    # --------------------------------------------------------------------------------
    # Leetcode 215. Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        aList = nums[:k]
        heapq.heapify(aList)
        
        # O( (N-K)logK )
        for i in range (k, len(nums)):
            heapq.heappush(aList, nums[i])
            heapq.heappop(aList)
            
        return heapq.heappop(aList)


    # --------------------------------------------------------------------------------
    # Leetcode 767. Reorganize String
    def reorganizeString(self, S: str) -> str:
        # count the frequency of each letter and append it into a list
        # count must be negative because it's a min heap 
        pq = []
        for x in set(S):
            pq.append( (-S.count(x), x) )

        # print(pq)

        # organized by frequency
        heapq.heapify(pq)

        # if there is a letter that occurs for more than half of len(S), it means there is no 
        # possible way to rearrage the letter
        if any( -count > (len(S) + 1) / 2 for count, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            # pop out the 2 char with highest frequency
            count1, char1 = heapq.heappop(pq)
            count2, char2 = heapq.heappop(pq)

            print( ans, char1, count1, char2, count2 )

            # add those 2 char to the end of ans string
            ans.extend( [char1, char2] )
            # since we just used them 2, decrease the frequency (frq is negative so adding 1 means decrease here)
            count1 += 1
            count2 += 1
            # if there is still some of that char left, push it back into the heap
            if count1: 
                heapq.heappush(pq, (count1, char1))
            if count2: 
                heapq.heappush(pq, (count2, char2))

        return "".join(ans) + (pq[0][1] if pq else '') 
        

    # --------------------------------------------------------------------------------
    # Leetcode 378. Kth Smallest Element in a Sorted Matrix
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat_matrix = []
        for array in matrix:
            flat_matrix.extend( [-1 * x for x in array] )

        # bring it back to find Kth largest element
        k_heap = flat_matrix[:k]
        heapq.heapify(k_heap)

        for i in range (k, len(flat_matrix)):
            heapq.heappush( k_heap, flat_matrix[i] )
            heapq.heappop( k_heap )

        return -1 * k_heap[0]

    # Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
    def kthSmallest_follow_up(self, matrix, k):
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        # a way to traverse NxN matrix in O(N) (instead of O(N^2))
        def countLessEqual(mid):
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        # binary search on the smallest and largest element of the array
        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
    

    # --------------------------------------------------------------------------------
    # Leetcode 373. Find K Pairs with Smallest Sums
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Since both nums 1 and nums2 are sorted, we can first create a heap out of all pairs between
        nums2[0] (j = 0) and elements in nums1. (i = 0,1,2,...,len-1)
        Then bring it back to the Kth largest element problem
        Pop [i][j] out then push [i][j+1] in
        """
        l1, l2 = len(nums1), len(nums2)

        # in case nums 1 or nums2 is empty
        if not l1 or not l2:
            return []
        
        # create a list for heap
        pairs = [ ( nums1[i] + nums2[0], i, 0) for i in range (l1) ]

        # create a heap
        heapq.heapify(pairs) # O( l1 )

        # bring back the old Kth largest/smallest problem
        ans = []
        while k > 0 and pairs:  # O(k)
            # pop
            sum, i, j = heapq.heappop(pairs)
            # append answer
            ans.append( [nums1[i], nums2[j]] )
            # push
            if j + 1 < l2:
                heapq.heappush(pairs, ( nums1[i] + nums2[j+1], i, j+1 ) ) 
            # update k
            k -= 1
        
        return ans


    # --------------------------------------------------------------------------------
    # Leetcode 347. Top K Frequent Elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        
        for num in nums:                # O(n)
            if num not in freq_dict:
                freq_dict[num] = 0
            else:
                freq_dict[num] -= 1     # this is a min heap
        
        heap = list()
        for key in freq_dict:   # O(n)
            heap.append( (freq_dict[key], key) )

        heapq.heapify(heap)     # O(n)

        answer = list()
        for i in range(k):
            pair = heapq.heappop(heap)
            answer.append(pair[1])

        return answer


    # --------------------------------------------------------------------------------
    # Leetcode 23. Merge k Sorted Lists
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # ----------------------------------------------
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        # ----------------------------------------------
        heap = []
        for node in lists:      # O(k)
            if node:
                heapq.heappush(heap, Wrapper(node))

        dummy = ListNode()      # to keep track of the head
        current = dummy
        while len(heap) != 0:
            node = heapq.heappop(heap).node
            current.next = node
            current = current.next
            if node and node.next: heapq.heappush(heap, Wrapper(node.next))

        return dummy.next

    # follow up: merge in place
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Refer back to our 'lists' variable for all the heads
        # Dict: value -> index of head in 'lists'
        '''
        lists = [ 2, 3]
        valueToIndexHead = {1:[node1, node2]}
        '''
        # Heap of fixed size k, where k == len(lists)
        # Our heap will only do comparison with the node value
        heap = []
        for i, head in enumerate(lists):
            if head:
                # (node.val, index of the linkedlist the node belongs to in our 'lists')
                heap.append((head.val, i)) 

        # Merge in place
        heapq.heapify(heap)         # O(n)
        current = ListNode()
        head = current
        while heap:
            val, i = heapq.heappop(heap)           
            current.next = lists[i]                 # Retrieve the node 
            current = current.next                  # Update current
            lists[i] = lists[i].next                # Update node in 'lists'
            if lists[i]:                            # Add another node to heap to maintain size k
                heapq.heappush(heap, (lists[i].val, i))
        
        return head.next

    # --------------------------------------------------------------------------------
    # Leetcode 973. K Closest Points to Origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        # compute distance between point and origin and add it to the heap
        for i, point in enumerate(points):
            x, y = point
            distance = ((x**2) + (y**2))**(1/2)
            heapq.heappush( heap, (distance, i) )
        
        # retrieve the k closest points to origin
        ans = []
        for c in range(k):
            dis, ind = heapq.heappop(heap)
            ans.append( points[ind] )

        return ans

    # --------------------------------------------------------------------------------    
    # Leetcode 659. Split Array into Consecutive Subsequences
    # def isPossible(self, nums: List[int]) -> bool:

    # --------------------------------------------------------------------------------    
    # Leetcode 692. Top K Frequent Words
    def topKFrequent(self, words, k):
        # Step 1: Count frequency of each word
        freq = collections.Counter(words)  # Dictionary-like object: {word: count}

        # Step 2: Define a custom comparator using a tuple
        # Python's heapq is a min-heap, so we invert frequency to simulate max-heap behavior
        # We use (-count, word) so that:
        #   - Higher frequency comes first (because of negative count)
        #   - Lexicographically smaller word comes first in case of tie
        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))
            # Optional: If you want to limit heap size to k (like in C++), use:
            # if len(heap) > k:
            #     heapq.heappop(heap)

        # Step 3: Extract top k elements from the heap
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])  # Only take the word part

        return result


    # --------------------------------------------------------------------------------
    # Leetcode 621. Task Scheduler
    # In this problem, we don't care about task label. We only care about the frequency of each task,
    # which helps us compute the min # of interval required to complete all tasks
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)

        # This min heap only contains the frequency of each task.
        # We want to prioritize processing the task with highest freq left (also greedy approach)
        heap = []
        for _, f in freq.items():
            heap.append(-f)        
        heapq.heapify(heap)             # O(n)

        time = 0
        dq = collections.deque()        # Contains (freq of a task, timestamp when this task can start being processed again)
        while heap or dq:
            time += 1

            # 1. Check if any task ready to be processed again
            # We only have to check one task because there cannot be two task with the same timestamp
            if dq and dq[0][1] == time:
                pop = dq.popleft()
                heapq.heappush(heap, pop[0])

            # 2. Process one of the available task
            if heap:
                f = heapq.heappop(heap)

                # We now have one less of this task to process, but only add it back to the queue if there is still some of this tasks to process
                if f + 1 < 0:
                    dq.append((f+1, time + n + 1))

        return time
            
            






        




















if __name__ == "__main__":
    leetcode = Solution()

    # --------------------------------------------------------------------------------
    #lc767 = 'aab'
    #reorganized = leetcode.reorganizeString(lc767)
    #print(reorganized)

    # --------------------------------------------------------------------------------
    #lc378 = [[1,5,9],[10,11,13],[12,13,15]]
    #k = 8
    #kthSmallest = leetcode.kthSmallest( lc378, k )
    #print(kthSmallest)

    # --------------------------------------------------------------------------------
    # lc373_nums1 = [1,7,11]
    # lc373_nums2 = [2,4,6]
    # k = 3
    # kpairs_smallest = leetcode.kSmallestPairs(lc373_nums1, lc373_nums2, k)
    # print(kpairs_smallest)

    # --------------------------------------------------------------------------------
    # nums = [3,2,1,5,6,4]
    # k = 2
    # leetcode.findKthLargest(nums, k)

    # --------------------------------------------------------------------------------
    medianFinder = MedianFinder()
    medianFinder.addNum(1)    
    medianFinder.addNum(2)  
    medianFinder.findMedian()
    medianFinder.addNum(3)
    medianFinder.findMedian()
    medianFinder.addNum(4)
    medianFinder.addNum(5)
    medianFinder.addNum(6)
    medianFinder.addNum(7)
    medianFinder.addNum(8)
    medianFinder.addNum(9)
    medianFinder.addNum(10)
    medianFinder.findMedian()

