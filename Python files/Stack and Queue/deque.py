"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================================ Queue ============================================================

Template 
monotonicQueueTemplate()
dualMonotonicWindow()

All LC questions below follow the monotonic queue template

(Medium)
Leetcode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Leetcode 2762. Continuous Subarrays

(Hard)
Leetcode 239. Sliding Window Maximum
Leetcode 862. Shortest Subarray with Sum at Least K

"""

from typing import List
from collections import defaultdict, deque
import bisect


class Solution:
    def monotonicQueueTemplate(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices of candidates in decreasing order
        result = []

        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Maintain decreasing order: remove smaller elements from the back
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Record result once the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])  # front is the max in the window

        return result

    """
    Find the maximum length of a subarray [left, right] such that the constraint function constraint_fn(max, min) returns True.
    """
    def dualMonotonicWindow(self, nums: List[int], constraint_fn) -> int:
        # Keeps track of indices in decreasing order → gives the maximum in the current window
        max_dq = deque()
        # Keeps track of indices in increasing order → gives the minimum in the current window
        min_dq = deque()  
        # 'left' indice shrinks the window when the constraint is violated
        left = 0
        best = 0

        for right in range(len(nums)):
            # 1+2. Maintain decreasing order for max
            while max_dq and nums[right] > nums[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(right)
 
            # 1+2. Maintain increasing order for min
            while min_dq and nums[right] < nums[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(right)

            # 3. Shrink window until constraint is satisfied
            while not constraint_fn(nums[max_dq[0]], nums[min_dq[0]]):
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()

            # 4. Update result
            best = max(best, right - left + 1)

        return best


    # --------------------------------------------------------------------------------------------
    # Leetcode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Each queue will be storing the max and min of each sliding window
        increasing_dq, decreasing_dq = deque(), deque()
        longestSubarrayLen = 1
        left = 0

        for right in range (len(nums)):
            # 1. Maintain the increasing/decreasing order
            while increasing_dq and nums[right] <nums[increasing_dq[-1]]:
                increasing_dq.pop()
            while decreasing_dq and nums[right] > nums[decreasing_dq[-1]]:
                decreasing_dq.pop()

            # 2. Append the current index
            increasing_dq.append(right)
            decreasing_dq.append(right)

            # 3. Remove invalid indices
            while abs( nums[decreasing_dq[0]] - nums[increasing_dq[0]] ) > limit:
                # Move left pointer forward
                left += 1
                # Remove out-of-window indices
                if decreasing_dq[0] < left:
                    decreasing_dq.popleft()
                if increasing_dq[0] < left:
                    increasing_dq.popleft()

            # 4. Record the results
            longestSubarrayLen = max(longestSubarrayLen, right-left+1)

            # If this problem is asking for len of the shortest subarray, then use below code
            # currentMaxIndex = decreasing_dq[0]
            # currentMinIndex = increasing_dq[0]
            # longestSubarrayLen = max(longestSubarrayLen, abs(currentMinIndex-currentMaxIndex)+1)

        return longestSubarrayLen

    # --------------------------------------------------------------------------------------------
    # Leetcode 2762. Continuous Subarrays
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_dq, min_dq = deque(), deque()
        left = 0
        count = 0

        for right in range (len(nums)):
            # 1. Maintain the order of two monotonic queue
            while min_dq and nums[right] < nums[min_dq[-1]]:
                min_dq.pop()
            while max_dq and nums[right] > nums[max_dq[-1]]:
                max_dq.pop()

            # 2. Append the next element to each queue
            min_dq.append(right)
            max_dq.append(right)

            # 3. Remove invalid index
            while nums[max_dq[0]] - nums[min_dq[0]] > 2:
                # Move left pointer
                left += 1
                # Remove invalid index
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
            
            # 4. Update the result: new subarray [left,right] satisfy the condition
            # ==> It will contribute (right-left+1) subarrays ending at right
            count += (right-left+1)

        return count

    # --------------------------------------------------------------------------------------------
    # Leetcode 3578. Count Partitions With Max-Min Difference at Most K
    def countPartitions(nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        f = [0] * (n + 1)  # f[i] = number of ways to partition first i elements
        g = [0] * (n + 1)  # g[i] = prefix sum of f[0..i]
        f[0] = 1
        g[0] = 1

        max_dq, min_dq = deque()
        left = 0

        for right in range(1, n + 1):
            num = nums[right - 1]

            # 1+2. Maintain max queue
            while max_dq and num > max_dq[-1]:
                max_dq.pop()
            max_dq.append(num)

            # 1+2. Maintain min queue
            while min_dq and num < min_dq[-1]:
                min_dq.pop()
            min_dq.append(num)

            # 3. Shrink window until valid
            while max_dq[0] - min_dq[0] > k:
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1

            # 4. DP transition
            f[right] = (g[right - 1] - (g[left - 1] if left > 0 else 0)) % MOD
            g[right] = (g[right - 1] + f[right]) % MOD

        return f[n]
    


    # ============================================================================================
    # Leetcode 239. Sliding Window Maximum - Hard
    # https://www.geeksforgeeks.org/dsa/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
    # Solution 1: Max-heap - O(nlogn): Inserting an element in heap takes (log n) time and we are inserting all n elements, thus the time complexity will be O(n * log n).
    # Solution 2 (this implementation): Deque - O(n) time and O(k) space
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a deque to store only the index of useful elements of CURRENT WINDOW 
        # An element is useful if it is in current window and is greater than all other elements on right side of it in current window.
        # At any point, our queue can have at most k elements
        dq = deque([])

        # Step 2: Run a loop and insert the first k elements in the deque
        for i in range (k):
            # Before inserting the element, check if the element at the back of the queue is smaller than the current element. 
            # If it is so remove the element from the back of the deque until all elements left in the deque are greater than the current element.
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()    # Important: remove from rear
            
            dq.append(i)

        # Step 3: run a loop from k to the end of the array
        result = []
        for i in range (k, len(nums)):
            # The element at the front of the queue is the largest element of previous window, so store it
            result.append(nums[dq[0]])

            # Remove the elements that are out of current window
            while dq and dq[0] <= i-k:
                dq.popleft()

            # Remove useless elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()    # Important: remove from rear

            dq.append(i)

        # For the last window
        result.append(nums[dq[0]])

        return result


    # --------------------------------------------------------------------------------------------
    # Leetcode 862. Shortest Subarray with Sum at Least K - Hard
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Prefix sums to compute subarray sums in constant time
        prefixSum = [None for _ in range (len(nums)+1)]         # PrefixSum needs to have length of (n+1) instead of n
        prefixSum[0] = 0
        prefixSum[1] = nums[0]          
        for i in range (2, len(prefixSum)):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]            
        print(prefixSum)

        # A monotonic increasing deque to track candidate starting indices for subarrays
        # Why monotonic? What make an indice 'i' "better" than indice 'j'
        #   If prefixSum[i] ≤ prefixSum[j], then i is a better starting point than j for future subarrays.
        #   We remove worse candidates from the back of the deque.
        min_dq = deque()
        ans = len(nums) + 1
        
        # Iterate through prefixSum
        for i in range (len(prefixSum)):
            # 3+4. Shrink window while condition is still satisfied and update ans
            # min_dq[0] here is the CURRENT best indice to start our subarray
            while min_dq and (prefixSum[i] - prefixSum[min_dq[0]]) >= k:
                startIndex = min_dq.popleft()
                ans = min(ans, (i-startIndex))

            # 1. Maintain the order of our queue 
            # min_dq[-1] here is the CURRENT worst indice to start our subarray
            while min_dq and prefixSum[i] <= prefixSum[min_dq[-1]]:
                min_dq.pop()
            
            # 2. Append i to the queue
            min_dq.append(i)

        return ans if ans != len(nums)+1 else -1






















# =================================================================================================================================================
# =================================================================================================================================================















if __name__ == "__main__":
    leetcode = Solution()

    # ---------------------- 239 ----------------------
    # nums = [1,3,-1,-3,5,3,6,7]
    # k = 3
    # print(leetcode.maxSlidingWindow(nums, k))

    # ---------------------- 1438 ----------------------
    # nums = [10,1,2,4,7,2]
    # limit = 5
    # print(leetcode.longestSubarray(nums, limit))

    # ---------------------- 2762 ----------------------
    # nums = [5,4,2,4]
    # print(leetcode.continuousSubarrays(nums))

    # ---------------------- 862 ----------------------
    nums = [10,1,-2,4,7,2]
    k = 12
    print(leetcode.shortestSubarray(nums, k))


