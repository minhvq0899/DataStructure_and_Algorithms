"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Binary Search =========================================================


"""

from typing import List
import bisect


# nums is an array, target is an integer
def binarySearch(nums, target):
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


# bisect left: 
# if found the value, return the index
# if don't found the value, return the index of the closest larger value
def bs_left(nums, target):
    left = 0
    right = len(nums)  - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target and (mid == left or nums[mid] > nums[mid-1]):
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



# bisect right: ALWAYS return the index of closest larger value
def bs_right(nums, target):
    left = 0
    right = len(nums)  - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target and (mid == right or nums[mid] < nums[mid+1]):
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1    



# Leetcode 34. Find First and Last Position of Element in Sorted Array
def searchRange(nums: List[int], target: int) -> List[int]:
    i = bisect.bisect_left(nums, target)
    j = bisect.bisect_right(nums, target)
    
    if i == j: # doesn't find the target value
        return [-1, -1]
    else:
        return [i, j-1]




    

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











