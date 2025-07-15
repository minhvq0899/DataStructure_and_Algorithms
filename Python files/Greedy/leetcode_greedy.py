"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Greedy =========================================================

1. Leetcode 121. Best Time to Buy and Sell Stock
2. Leetcode 56. Merge Intervals
3. Leetcode 1710. Maximum Units on a Truck
4. Leetcode 1029. Two City Scheduling
5. Leetcode 45 Jump Game II


"""

from typing import List
import heapq

class Solution:
    # Leetcode 121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0
        
        for i in range (0, len(prices)):
            if prices[i] <= low:
                low = prices[i]
            elif(prices[i] - low > max_profit):
                max_profit = prices[i] - low
            
        return max_profit

    # -------------------------------------------------------------------------
    # Leetcode 56. Merge Intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # sort intervals by the start time
        intervals.sort(key=lambda x: [x[0]])
        
        print(intervals)
        
        res.append(intervals[0])
        # now loop through intervals
        for i in range (len(intervals) - 1):
            # first append the next interval
            res.append(intervals[i+1])
            
            # if end time overallaps with the next start time -> merge
            print(str(i), "time: ", res[-2][1], res[-1][0] )
            if res[-2][1] >= res[-1][0]:
                after = res.pop()
                before = res.pop()
                res.append([before[0], max(before[1], after[1])])
        
        return res

    # -------------------------------------------------------------------------
    # Leetcode 1710. Maximum Units on a Truck
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort( key=lambda x: -x[1] )
        max_units = 0
        box = 0
        
        while truckSize > 0 and box < len(boxTypes):
            if boxTypes[box][0] <= truckSize: 
                max_units += boxTypes[box][0] * boxTypes[box][1]
            else: 
                max_units += truckSize * boxTypes[box][1]
                
            truckSize -= boxTypes[box][0]
            box += 1
        
        return max_units

    # -------------------------------------------------------------------------
    # Leetcode 1029. Two City Scheduling
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        The delta between the costs to A and B is what matters the most.
        """
        n = len(costs)
        # this is how much more expensive to send that person to A instead of B
        delta = [a - b for [a, b] in costs] # O(n)
        # now create a list to store delta with its index
        delta_index = []
        for i in range (n): # O(n)
            delta_index.append( [delta[i], i] )

        # now sort that delta_index
        delta_index.sort( key=lambda x: x[0]) # O(nlogn)
        
        # now your delta is sorted from cheapest to go to A --> most expensive to go to A
        # just have to send the first half to A and the second half to B
        mincost = 0 
        for i in range (n):
            index = delta_index[i][1]
            if i < n/2: 
                mincost += costs[index][0]
            else:
                mincost += costs[index][1]

        return mincost

    # -------------------------------------------------------------------------
    # Leetcode 45 Jump Game II
    def jump(self, nums: List[int]) -> int:
        jumps = 0         # Total jumps made
        farthest = 0      # Furthest index reachable in current window
        end = 0           # End of current jump window

        for i in range(len(nums) - 1):  # No need to jump from last index
            farthest = max(farthest, i + nums[i])  # Update furthest reach

            if i == end:
                jumps += 1       # Time to jump
                end = farthest   # Update window

        return jumps



if __name__ == "__main__":
    leetcode = Solution()

    # --------------------------------------------------------------------
    # costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    # mincost = leetcode.twoCitySchedCost(costs)
    # print("\nMin cost: ", mincost)











