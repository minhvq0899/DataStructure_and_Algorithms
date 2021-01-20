"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Heap  =========================================================
1. Leetcode 215. Kth Largest Element in an Array
2. Leetcode 767. Reorganize String
3. Leetcode 378. Kth Smallest Element in a Sorted Matrix
4. Leetcode 373. Find K Pairs with Smallest Sums


"""

from typing import List
import heapq

class Solution:
    # Leetcode 215. Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        aList = nums[:k]
        heapq.heapify(aList)
        
        for i in range (k, len(nums)):
            heapq.heappush(aList, nums[i])
            heapq.heappop(aList)
            
        return heapq.heappop(aList)


    # Leetcode 767. Reorganize String
    def reorganizeString(self, S: str) -> str:
        # count the frequency of each letter and append it into a list
        # count must be negative because it's a min heap 
        pq = []
        for x in set(S):
            pq.append( (-S.count(x), x) )

        print(pq)

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
            # since we just used them 2, decrease the frequency
            count1 += 1
            count2 += 1
            # if there is still some of that char left, push it back into the heap
            if count1: 
                heapq.heappush(pq, (count1, char1))
            if count2: 
                heapq.heappush(pq, (count2, char2))

        return "".join(ans) + (pq[0][1] if pq else '') 
        
        
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
        heapq.heapify(pairs) # O(n)

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
    lc373_nums1 = [1,7,11]
    lc373_nums2 = [2,4,6]
    k = 3
    kpairs_smallest = leetcode.kSmallestPairs(lc373_nums1, lc373_nums2, k)
    print(kpairs_smallest)




