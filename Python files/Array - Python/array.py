"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Array =========================================================

1. Leetcode 15: 3Sum
    a) Approach 1: Two pointer -> sort needed
    b) Approach 2: Hashset but sort needed
    c) Approach 3: Hashset but sort isn't needed
2. Leetcode 
3. Leetcode 152: 

"""

from typing import List

class Solution:
    # Leetcode 15. 3Sum
    # # Aprroach 1: Two pointer -> sort the array
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     # O(n)
    #     # ----------------------------------------------------------
    #     def helper2Sum(nums, i, result):
    #         lo, hi = i+1, len(nums)-1
    #         while lo < hi:
    #             if nums[lo] + nums[hi] < -nums[i]:
    #                 lo += 1
    #             elif nums[lo] + nums[hi] > -nums[i]:
    #                 hi -= 1
    #             else:
    #                 result.append([nums[i], nums[hi], nums[lo]])
    #                 lo += 1
    #                 while lo < hi and nums[lo] == nums[lo-1]:
    #                     lo += 1
    #     # ----------------------------------------------------------
    #     # Sort: O(nlog(n))
    #     nums.sort()
    #     # Two pointers
    #     result = list()
    #     # O(n^2)
    #     for i, val in enumerate(nums):
    #         if val > 0: break
    #         if i == 0 or nums[i] != nums[i-1]:
    #             helper2Sum(nums, i, result)
        
    #     return result

    # Aprroach 2: Hashset but sort needed
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
    



























if __name__ == "__main__":
    leetcode = Solution()

    # --------------------------------------------------------------------










