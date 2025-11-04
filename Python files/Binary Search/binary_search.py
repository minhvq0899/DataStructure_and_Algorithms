"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Binary Search =========================================================
1. Classic Binary Search - find the exact match

2. Lower Bound Search - first index where the value is >= the target (bisect left) 
Behavior: 
- if found the value, return the index
- if couldn't find the value, return the index of the closest larger value
🔍 bs_left: Find the first position where a value could go
- Think: “Where can I insert this value so it appears before any existing duplicates?”
- Use case: Lower bound, weighted sampling, prefix sum searc

3. Upper Bound Search - last index where the value is <= the target (bisect right) 
🔍 bs_right: Find the last position where a value could go
- Think: “Where can I insert this value so it appears after any existing duplicates?”
- Use case: Upper bound, range queries, histogram binning

🧪 Example
arr = [1, 2, 2, 2, 3]
target = 2

bs_left(arr, target) -> 2
bs_right(arr, target) -> 4



"""

from typing import List
import bisect

bisect.bisect_left()

# 1. Classic Binary Search - find the exact match
def binarySearch(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = left + (right-left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1    


"""
Note: 
1. In both algorithms below, you can never set 'left' == 'mid' because the division to find 'mid' 
always rounds down. If left == 0 and right == 1, setting 'left' == 'mid' will cause infinite loop.

2. The reason why we set right = len(nums) and not len(nums)-1 is explained below
"""
# 2. Lower Bound Search - first index where the value is >= the target (bisect left) 
def bs_left(nums: List[int], target: int) -> int:
    # 'right' starts at len(nums) here because the output can be len(nums)
    left, right = 0, len(nums)  

    while left < right:
        mid = (left + right) // 2

        # Case 1: target is after mid
        if nums[mid] < target:
            left = mid + 1
        # Case 2: target is before mid -> we found a "candidate"
        else:
            right = mid

    # Once 'left' == 'right', we've found the smallest index where target <= nums[i] 
    # Since the while loop stops precisely at the first time 'left' == 'right', 
    # it is also okay to return 'right' instead of 'left' 
    return left     



"""
By setting right = len(nums), we allow the search to consider the position just beyond the last index — which is valid when:
- The target is larger than all elements (so the answer is len(nums))
- Or smaller than all elements (so the answer is 0)
"""
# 3. Upper Bound Search - last index where the value is <= the target (bisect right) 
def bs_right(nums: List[int], target: int):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        # Case 1: target is after mid 
        if nums[mid] <= target:
            left = mid + 1
        # Case 2: target < nums[mid]
        # Found a candidate
        else:
            right = mid

    # Since the while loop stops precisely at the first time 'left' == 'right', 
    # it is also okay to return 'right' instead of 'left'
    return left    






if __name__ == "__main__":
    # nums = [-9, -2, 1, 4, 5, 6, 8, 9, 10, 13, 20, 30]
    # target = 9

    # print(binarySearch(nums, target))

    nums = [-9, -2, 1, 4, 5, 6, 6, 6, 6, 6]
    target = 6

    print(bs_right(nums, target))

    # nums = [5,7,7,8,8,10]
    # target = 8

    # print(searchRange(nums, target))











