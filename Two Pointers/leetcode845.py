"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================== Two Pointers Exercise ==============================================
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. 
Return 0 if there is no mountain subarray.

"""
from typing import List

def longestMountain(arr: List[int]) -> int:
    i, j = 0, 0
    while i < len(arr) - 2:
        while i < len(arr) - 1 and arr[i] >= arr[i+1]: 
            i += 1
            j += 1

        count = 0
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            count += 1
            i += 1

        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            count -= 1
            i += 1

        if count == 0: 
            return (i-j+1) if (i-j+1) >= 3 else 0
        else: 
            j = i
            
    return 0


if __name__ == "__main__":
    #arr = [2,2,2]
    #print(longestMountain(arr))

    i = 2
    j = 1
    longest = (i-j+1) if (i-j+1) >= 3 else 0
    print(longest)


