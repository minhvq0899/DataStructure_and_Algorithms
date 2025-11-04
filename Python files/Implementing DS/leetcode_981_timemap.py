"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode 981. Time Based Key-Value Store =========================================================
HashMap + Binary Search


"""

from collections import defaultdict

"""
5, 10, 15
target = 4
left = 0
right = 0
mid = 0
"""
class TimeMap:
    def __init__(self):
        # key -> [(timestamp1, value1), (timestamp2, value2), etc]
        self.globalMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.globalMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        valueList = self.globalMap[key]
        if not valueList:
            return ""
        
        # Find the last index where the value is <= the target timestamp (bisect right) 
        left, right = 0, len(valueList)
        while left < right:
            mid = (left + right) // 2

            # Case 1: If nums[mid] ≤ target, we want to search right side
            if valueList[mid][0] <= timestamp:
                left = mid + 1
            # Case 2: Found a candidate
            else:
                right = mid

        # After loop, left is the first index where target < nums[i]
        # So the last index where nums[i] ≤ target is (left - 1)

        # If no value inserted before the target timestamp
        if left == 0:
            return ""
        
        return valueList[left - 1][1]

        











if __name__ == "__main__":







