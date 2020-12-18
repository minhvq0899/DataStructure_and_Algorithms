"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================== Two Pointers Exercise ==============================================
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
Using two pointers, we can reduce from O(n^2) down to O(n)

1. Easy: all integers in nums are positive
2. Medium: integers in nums can be negative
"""
from typing import List

class subarraySumEqualsK:
    # [1,2,6,3,5,1,8,9] with K = 9
    def easy(self, nums: List[int], K: int) -> int:
        i, j = 0, 0
        sum = 0
        cnt = 0 # counts of subarray
        while i < len(nums): 
            if sum + nums[i] < K:
                sum += nums[i]
                i += 1
            elif sum + nums[i] > K:
                sum -= nums[j]
                j += 1
            else: # this covers for when sum + nums[i] == K  --> we found another subarray
                cnt += 1
                sum += nums[i]
                i += 1
            
        return cnt

    def medium(self, nums: List[int], K: int) -> int:
        pass
    
if __name__ == "__main__":
    nums = [1,2,6,3,5,1,8,9] 
    subarray_obj = subarraySumEqualsK()
    print(subarray_obj.easy(nums, 9))
    print("hello \n")

    for k in range(len(nums), 0, -1):
        print(k)


















