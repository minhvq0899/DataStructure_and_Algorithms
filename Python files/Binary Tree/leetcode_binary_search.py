"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Search  =========================================================
1. Leetcode 875. Koko Eating Bananas
2. Leetcode 35. Search Insert Position

"""

from typing import List


class Solution:
    # Leetcode 875. Koko Eating Bananas
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # helper function to decide if possible to eat all bananas with k 
        # bananas/ hour
        def possible (k):
            hour = 0
            for pile in piles:
                if pile % k == 0:
                    hour += pile / k
                else:
                    hour += (pile // k) + 1
            
            return True if hour <= h else False
        # ----------------------------------------------------------------
        
        # do binary search on k
        right = max(piles) # right bound
        left = 1
        ans = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            if possible(mid): # we can do better
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
            
        return ans

    # Leetcode 35. Search Insert Position
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
        
        return left

    # Leetcode 1011. Capacity To Ship Packages Within D Days
    def possible(self, weights: List[int], days: int, capacity: int) -> bool:
        temp_cap = capacity
        count_day = 0
        idx = 0
        while idx < len(weights):
            temp_cap -= weights[idx]
            if temp_cap >= 0:
                idx += 1
            else:
                count_day += 1
                temp_cap = capacity
        
        if temp_cap < 0:
            return False
        else:
            return True if count_day + 1 <= days else False  
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        cap = max_cap
        while (min_cap <= max_cap):
            mid = min_cap + (max_cap - min_cap) // 2
            print(mid)
            if self.possible(weights, days, mid):
                max_cap = mid - 1
                cap = min(cap, mid)
                print("possible")
            else:
                min_cap = mid + 1

            print(mid)

        return cap













if __name__ == "__main__":
    leetcode = Solution()

    # ---------------------- 35 ----------------------
    # idx = leetcode.searchInsert( [1,3,5,6], 2 )
    # print(idx)

    # ---------------------- 1011 ----------------------
    # print( "Final: ", leetcode.shipWithinDays_test( [3,2,2,4,1,4], 3 ) )

    # ---------------------- 875 ----------------------
    print( "Final: ", leetcode.minEatingSpeed( [312884470], 312884469 ) )


