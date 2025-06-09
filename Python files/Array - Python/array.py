"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Array =========================================================

1. Leetcode 15: 3Sum
    a) Approach 1: Two pointer -> sort needed
    b) Approach 2: Hashset but sort needed
    c) Approach 3: Hashset but sort isn't needed
2. 
    (Easy) Leetcode 448. Find All Numbers Disappeared in an Array
    (Medium) Leetcode 442. Find All Duplicates in an Array
    (Hard) Leetcode 41. First Missing Positive
3. Leetcode 152: Maximum Product Subarray
4. Leetcode 238. Product of Array Except Self
5. Leetcode 567. Permutation in String

"""

from typing import List
from collections import Counter
import copy

class Solution:
    # ------------------------------------------------------------------------------
    # Leetcode 15. 3Sum
    # Aprroach 1: Two pointer -> sort the array
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        nums.sort() 
        ans = []
        # ------------------------------------------------------------------------
        def helper2Sum(i):
            lo, hi = i+1, len(nums) - 1

            # Ex: if 2sum is 1, then we are looking for -1 to make the sum as 0. 
            while lo < hi:
                if nums[lo] + nums[hi] < -nums[i]:
                    lo += 1
                elif nums[lo] + nums[hi] > -nums[i]:
                    hi -= 1
                else:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
        # ------------------------------------------------------------------------
        # O(N^2)
        for i, val in enumerate(nums):
            if val > 0: break # since we are looking for triplet with sum 0, if the smallest item is > 0 already, then no triplet possible
            if i == 0 or nums[i] != nums[i-1]:
                helper2Sum(i)
        
        return ans

    # Aprroach 2: Hashset but sort needed
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        # Sort: O(nlog(n))
        nums.sort()

        # O(n^2)
        solution = []
        for i, val_i in enumerate (nums):
            target = 0 - val_i
            print("target: ", target)
            complement_dict = dict()
            seen = set()
            for k, val_k in enumerate (nums):
                if k != i and k not in seen:
                    seen.add(k)
                    complement = target - val_k
                    if val_k in complement_dict:
                        other = complement_dict[val_k]
                        solution.append([nums[i], nums[k], nums[other]])
                    else:
                        complement_dict[complement] = k
                    print(complement_dict)
                    print(solution)
                    
        return solution

    # ------------------------------------------------------------------------------
    # Leetcode 442. Find All Duplicates in an Array
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range (len(nums)):
            nums[abs(nums[i])-1] *= -1 
            if nums[abs(nums[i])-1] > 0:
                ans.append(abs(nums[i]))
            
        return ans
    
    # ------------------------------------------------------------------------------
    # Leetcode 41. First Missing Positive
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
    # Leetcode 152. Maximum Product Subarray
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currentMin, currentMax = 1, 1

        for n in nums:
            if n == 0: 
                currentMin, currentMax = 1, 1
                continue

            tmp = currentMax * n
            currentMax = max(currentMax * n, currentMin * n, n)
            currentMin = min(tmp, currentMin * n, n)
            res = max(res, currentMax)

        return res

    # ------------------------------------------------------------------------------
    # Leetcode 238. Product of Array Except Self
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        l = 1
        left[0] = 1
        for i in range (1, len(left)):
            left[i] = nums[i-1] * l
            l = left[i]

        right = [0] * len(nums)
        r = 1
        right[len(right)-1] = 1
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




























if __name__ == "__main__":
    leetcode = Solution()

    # --------------------------- 15 ---------------------------
    # nums = [-1,0,1,2,-1,-4]
    # print(leetcode.threeSum2(nums))

    # for i in range(128):
    #     print(f"{i}: {chr(i)}")

    # --------------------------- 41 ---------------------------
    nums = [1,1] #[3,4,-1,1]
    print(leetcode.firstMissingPositive(nums))

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





