"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Array =========================================================

Leetcode 15: 3Sum
    a) Approach 1: Two pointer -> sort needed
    b) Approach 2: Hashset but sort needed
    c) Approach 3: Hashset but sort isn't needed
Leetcode 18. 4Sum
Leetcode 454. 4Sum II
 
(Easy) Leetcode 448. Find All Numbers Disappeared in an Array
(Medium) Leetcode 442. Find All Duplicates in an Array
(Hard) Leetcode 41. First Missing Positive
Leetcode 287. Find the Duplicate Number 
Leetcode 457: Circular Array Loop
Leetcode 1060. Missing Element in Sorted Array

Leetcode 238. Product of Array Except Self
Leetcode 567. Permutation in String
Leetcode 128: Longest Consecutive Sequence
Leetcode 252: Meeting Rooms (Easy)
Leetcode 253: Meeting Rooms II

(Boyer-Moore majority vote algorithm)

Leetcode 229. Majority Element II
"""

from typing import List
from collections import Counter
import copy
import math

class Solution:
    # ------------------------------------------------------------------------------
    # Leetcode 15. 3Sum
    # Aprroach 1: Two pointer -> sort the array
    # 1. Sort the array.
    # 2. Fix the first element of the triplet using a loop.
    # 3. For the remaining array to the right of the fixed element, use two pointers (left, right) to find pairs that sum to -nums[i]
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        nums.sort() 
        ans = []
        # ------------------------------------------------------------------------
        def helper2Sum(i):
            lo, hi = i+1, len(nums) - 1

            # Ex: if 2sum is 1, then we are looking for -1 to make the sum as 0. 
            while lo < hi:
                # nums is sorted, so can perform two-pointer now
                if nums[lo] + nums[hi] < -nums[i]:
                    lo += 1
                elif nums[lo] + nums[hi] > -nums[i]:
                    hi -= 1
                else:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    # skip all dup
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
        # ------------------------------------------------------------------------
        # Step 2: Fix the first element of the triplet using a loop
        for i, val in enumerate(nums):
            # Optimization: since we are looking for triplet with sum 0, if the smallest item is > 0 already, then no triplet possible
            if val > 0: break 

            # Step 3: For the remaining array to the right of the fixed element, use two pointers (left, right) to find pairs that sum to -nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                helper2Sum(i)
        
        return ans

    # Aprroach 2: Hashset but sort needed
    # 1. Sort the array for consistency and duplicate control.
    # 2. For each index i, track all complements of target = -nums[i] using a HashSet.
    # 3. Avoid duplicates using a seen set and triplet deduplication logic.

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort the array for consistency and duplicate control ( O(nlog(n)) )
        nums.sort()
        solution = set()

        # 2. For each index i, track all complements of target = -nums[i] using a HashSet. ( O(n^2) )
        for i, val_i in enumerate (nums):
            # Optimization: since we are looking for triplet with sum 0, if the smallest item is > 0 already, then no triplet possible
            if val_i > 0: break 

            target = 0 - val_i
            seen = set()

            for j in range (i+1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    solution.add((nums[i], complement, nums[j]))

                # 3. Avoid duplicates using a seen set and triplet deduplication logic.
                seen.add(nums[j])
                    
        return list(list(s) for s in solution)

    # Generalize for kSum
    def kSum(self, nums: List[int], target: int, k: int) -> List[int]:
        # -------------------------------------------
        def ksum(start, target, k):
            res = []

            # Base case: solve 2Sum using the two-pointer technique
            if k == 2:
                left, right = start, len(nums) - 1
                while left < right:
                    sum_ = nums[left] + nums[right]
                    if sum_ == target:
                        # Found a valid pair
                        res.append([nums[left], nums[right]])

                        # Skip duplicate values for both pointers
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum_ < target:
                        # Move left pointer to increase sum
                        left += 1
                    else:
                        # Move right pointer to decrease sum
                        right -= 1
            # Recursive case: fix one number and solve (k - 1)Sum
            else:
                for i in range(start, len(nums) - k + 1):
                    # Prune early: skip duplicate fixed elements
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # Prune impossible cases: smallest possible sum is too big
                    if nums[i] * k > target:
                        break

                    # Prune impossible cases: largest possible sum is too small
                    if nums[-1] * k < target:
                        break

                    # Recursive call: solve (k - 1)Sum for remaining target
                    subsets = ksum(i + 1, target - nums[i], k - 1)
                    for subset in subsets:
                        # Combine fixed element with all subsets of size k - 1
                        res.append([nums[i]] + subset)

            return res
        # -------------------------------------------

        # Sort the array to enable two-pointer search and duplicate skipping
        nums.sort()

        # Kick off recursion from index 0
        return ksum(0, target, k)

    # ------------------------------------------------------------------------------
    # Leetcode 442. Find All Duplicates in an Array
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        # loop through each element
        for i in range (len(nums)):
            # mark nums[i] as visited by flipping the sign at (i-1)-th index
            nums[abs(nums[i])-1] *= -1  
            if nums[abs(nums[i])-1] > 0:
                ans.append(abs(nums[i]))
            
        return ans
    
    # ------------------------------------------------------------------------------
    # Leetcode 41. First Missing Positive (Hard)
    # Observation: If n = len(nums), then the ans to this problem can only be in range [1,n+1]
    # Corner case: nums[1,2,3,4] -> ans = 5
    def firstMissingPositive(self, nums: List[int]) -> int:
        # -------------------------------------------
        def swapping(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        # -------------------------------------------
        n = len(nums)

        # Keep swapping until every item goes to its right index spot (val go to nums[val-1] if val in range (1, n))
        for i in range (n):
            val = nums[i]
            while 0 < val and val < n+1 and nums[i] != nums[val-1]:
                swapping(i, val-1)
                val = nums[i]

        for i in range (n):
            if i+1 != nums[i]: return i+1

        return n+1

    # ------------------------------------------------------------------------------    
    # Leetcode 287. Find the Duplicate Number 
    # (must solve the problem without modifying the array nums and using only constant extra space)
    # treat array as a linked list
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize two pointers
        slow = nums[0]
        fast = nums[0]

        # Step 2: Move slow by 1 step, fast by 2 steps until they meet
        while True:
            slow = nums[slow]          # move 1 step
            fast = nums[nums[fast]]    # move 2 steps
            if slow == fast:
                break  # cycle detected

        # Step 3: Reset one pointer to the start
        slow = nums[0]

        # Step 4: Move both pointers 1 step at a time
        # They will meet at the cycle entrance — the duplicate
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    # ------------------------------------------------------------------------------    
    # Leetcode 457: Circular Array Loop
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        # Helper to get the next index in circular fashion
        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue  # Already visited or invalid

            direction = nums[i] > 0  # True for forward, False for backward
            slow, fast = i, next_index(i)

            # Move slow by 1 step, fast by 2 steps
            while (
                nums[fast] != 0 and
                nums[next_index(fast)] != 0 and
                (nums[fast] > 0) == direction and
                (nums[next_index(fast)] > 0) == direction
            ):
                if slow == fast:
                    # Check for loop length > 1
                    if slow == next_index(slow):
                        break
                    return True

                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # Mark all visited nodes as 0 to avoid reprocessing
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                next_j = next_index(j)
                nums[j] = 0
                j = next_j

        return False
    
    # ------------------------------------------------------------------------------    
    # Leetcode 1060. Missing Element in Sorted Array
    def missingElement(self, nums: List[int], k: int) -> int:
        # Helper to count how many numbers are missing before index i
        def missing(i):
            return nums[i] - nums[0] - i

        n = len(nums)

        # If k-th missing number is beyond the last element
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        # Binary search to find the smallest index where missing(i) >= k
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if missing(mid) >= k:
                right = mid
            else:
                left = mid + 1

        # The k-th missing number is after nums[left - 1]
        return nums[left - 1] + k - missing(left - 1)
    
    # ------------------------------------------------------------------------------
    # Leetcode 238. Product of Array Except Self
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        l = 1
        left[0] = 1

        # Populate the 'left' array
        for i in range (1, len(left)):
            left[i] = nums[i-1] * l
            l = left[i]

        right = [0] * len(nums)
        r = 1
        right[len(right)-1] = 1
        # Populate the 'right' array
        for i in range (len(right)-2, -1, -1):
            right[i] = nums[i+1] * r
            r = right[i]

        for i in range (len(left)):
            left[i] *= right[i]

        return left

    # ------------------------------------------------------------------------------
    # Leetcode 567. Permutation in String
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # Count freq of char in s1
        counterS1 = Counter(s1)
        counterS2 = Counter()

        # Use two pointer to check each substring of length len(s1) in s2
        # First populate Counter2
        i, j = 0, len(s1)-1
        for index in range (i, j+1):
            counterS2[s2[index]] += 1

        # print(counterS1)
        # print(counterS2)

        # Move two pointers
        while j < len(s2) - 1:
            if counterS1 == counterS2: return True
            
            counterS2[s2[i]] -= 1
            i += 1

            j += 1
            counterS2[s2[j]] += 1

        return counterS1 == counterS2

    # ------------------------------------------------------------------------------
    # Leetcode 128: Longest Consecutive Sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        # add all elements in nums in a set
        numsSet = set(nums)

        # variable to store answer
        maxLen = 0
        currentLen = 0

        # iterating over the set instead of the list because nums can contain dups
        for num in numsSet:
            # check if num is the beginning of a sequence
            if (num-1) not in numsSet:
                currentLen = 1
                current = num+1
                while (current in numsSet):
                    currentLen += 1
                    current += 1

                maxLen = max(maxLen, currentLen)

        return maxLen

    # ------------------------------------------------------------------------------
    # Leetcode 252: Meeting Rooms (Easy)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_interval = sorted(intervals, key=lambda x: x[0])
        # print(sorted_interval)

        for i in range (len(sorted_interval) - 1):
            if sorted_interval[i][1] > sorted_interval[i+1][0]:
                return False

        return True

    # ------------------------------------------------------------------------------
    # Leetcode 253: Meeting Rooms II
    # Follow Sweep line algorithm. Learn more about this algo with this playlist
    # https://leetcode.com/problem-list/ax36evp1/
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sortedStartingTime = sorted(list([i[0] for i in intervals]))
        sortedEndingTime = sorted(list([i[1] for i in intervals]))

        s, e = 0, 0
        res, count = 0, 0
        # sweep line algorithm
        while s < len(sortedStartingTime):
            # case 1: starting a new meeting
            if sortedStartingTime[s] < sortedEndingTime[e]:
                count += 1
                s += 1
            # case 2: a meeting ends
            else:
                count -= 1
                e += 1
            res = max(res, count)
        
        return res


    # ------------------------------------------------------------------------------
    # Leetcode 169. Majority Element I
    def majorityElement1(self, nums: List[int]) -> int:
        # Boyer–Moore majority vote algorithm
        count = 0
        candidate = None
        
        for num in nums:
            # that means before this index, all candidates have the same frequency
            if count == 0: 
                candidate = num
            count += (1 if candidate == num else -1)
        
        # Here we are returning candidate right away because the problem stated
        # "You may assume that the majority element always exists in the array"
        return candidate
    

    # ------------------------------------------------------------------------------
    # Leetcode 229. Majority Element II
    # If len(nums) == n, and we are looking for all elements that appear more than n/3 times, than there can only be at max 2 elements satisfy this condition.
    # Generalization for [n/k] threshold -> there can only be at max (k-1) elements. 
    # Similarly to LC 169, but this time create (k-1) 'candidates' and 'counts'
    # Idea is similar to keeping count in Counter/Hashmap (space complxity will be O(n)), but here we are only keeping count 
    # of the top (k-1) elemenents (space complexity will be O(1))
    def majorityElement2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        for num in nums:
            # If num is one of the candidates
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            # if one of the count is reset -> reset the candidate
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0: 
                candidate2 = num
                count2 = 1
            # else, decrement the freq of candidate1 and candidate2
            else:
                count1 -= 1
                count2 -= 1
        
        # Here, there can be AT MAX (k-1) result elements, but it doens't HAVE TO be (k-1)
        # So we need to validate
        return [x for x in (candidate1, candidate2) if nums.count(x) > n/3]











if __name__ == "__main__":
    leetcode = Solution()

    # --------------------------- 15 ---------------------------
    # nums = [-1,0,1,2,-1,-4]
    # print(leetcode.threeSum2(nums))

    # --------------------------- 41 ---------------------------
    # nums = [1,1] #[3,4,-1,1]
    # print(leetcode.firstMissingPositive(nums))

    # --------------------------- 152 ---------------------------
    # nums = [2, -3, 4, -1, -2, 1, 5]
    # print(leetcode.maxProductSubarray(nums))

    # --------------------------- 238 ---------------------------
    # nums = [1,2,3,4]
    # print(leetcode.productExceptSelf(nums))

    # --------------------------- 567 ---------------------------
    # s1 = "ab"
    # s2 = "bc"
    # print(leetcode.checkInclusion(s1, s2))

    # --------------------------- 169 + 229 ---------------------------
    nums = [1,2]
    result = leetcode.majorityElement2(nums)
    print(result)





