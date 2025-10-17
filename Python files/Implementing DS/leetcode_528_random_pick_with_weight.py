"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= 528. Random Pick with Weight =========================================================
This question is often asked during Meta interviews. 

"""

from typing import List
import random

# Solution 1: Binary Search
# Classic lower bound binary search:
# It finds the first index i such that prefixSum[i] >= target.
# It avoids out-of-bounds errors and handles all edge cases, including:
# - Single-element input
# - Duplicate weights
# - Large weights
class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = [0 for _ in range(len(w))]
        self.prefixSum[0] = w[0]
        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] = w[i] + self.prefixSum[i-1]
        
        print(self.prefixSum)

    def pickIndex(self) -> int:
        # Pick a randon int from the first and last value in our prefixSum
        target = random.randint(1, self.prefixSum[-1])

        # Now do Binary Search to find which partion does the random int belong to
        left, right = 0, len(self.prefixSum)-1
        while left < right:
            mid = (left+right) // 2
            
            if self.prefixSum[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left

        




if __name__ == "__main__":
    pass