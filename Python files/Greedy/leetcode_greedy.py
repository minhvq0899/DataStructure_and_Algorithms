"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Greedy =========================================================
Template function to find the local extrema    

    (Easy)
Leetcode 121. Best Time to Buy and Sell Stock
Leetcode 896. Monotonic Array
Leetcode 860. Lemonade Change
Leetcode 455. Assign Cookies

    (Medium)
    (Find localMin and localMax)
Leetcode 122. Best Time to Buy and Sell Stock II
Leetcode 845. Longest Mountain in Array
Leetcode 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Leetcode 162. Find Peak Element
Leetcode 1901. Find a Peak Element II

Leetcode 1276. Number of Burgers with No Waste of Ingredients
Leetcode 56. Merge Intervals
Leetcode 1710. Maximum Units on a Truck
Leetcode 1029. Two City Scheduling
Leetcode 55 Jump Game
Leetcode 45 Jump Game II

(Hard)
Leetcode 135. Candy


"""

from typing import List
import heapq
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Template function to find the local extrema
    def find_local_extrema(arr):
        n = len(arr)
        i = 0
        local_mins = []
        local_maxs = []

        while i < n - 1:
            # Find local min
            while i < n - 1 and arr[i] >= arr[i + 1]:
                i += 1
            if i < n:
                local_mins.append(i)

            # Find local max
            while i < n - 1 and arr[i] <= arr[i + 1]:
                i += 1
            if i < n:
                local_maxs.append(i)

        return local_mins, local_maxs

    # Leetcode 121. Best Time to Buy and Sell Stock
    def maxProfit121(self, prices: List[int]) -> int:
        # Initialize `low` to positive infinity — will store the lowest price seen so far
        low = float('inf')

        # Initialize `max_profit` to 0 — will store the max profit achievable
        max_profit = 0

        # Iterate through each day's stock price
        for i in range(len(prices)):
            # If today's price is less than or equal to `low`,
            # it becomes the new minimum buying price
            if prices[i] <= low:
                low = prices[i]
            # If selling today gives a better profit than our current max,
            # we update `max_profit`
            elif prices[i] - low > max_profit:
                max_profit = prices[i] - low

        # After checking all days, return the best possible profit
        return max_profit

    # Leetcode 860. Lemonade Change
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = { 5: 0, 10: 0, 20: 0 }

        for bill in bills:
            # if they pay $20
            if bill == 20:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[20] += 1
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[20] += 1
                    wallet[5] -= 3
                else: 
                    return False
            # if they pay $10
            elif bill == 10:
                if wallet[5] > 0:
                    wallet[10] += 1
                    wallet[5] -= 1
                else:
                    return False
            else: # if bill == 5
                wallet[5] += 1
        
        return True

    # Leetcode 455. Assign Cookies
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j = 0, 0

        while i < len(g) and j < len(s):
            if s[j] < g[i]:
                j += 1
            else: 
                i += 1
                j += 1
        
        return i + 1


    # =========================================================================
    # Leetcode 122. Best Time to Buy and Sell Stock II
    def maxProfit122(self, prices: List[int]) -> int:
        localMin, localMax = 0, 0           # These are indexes 
        profit = 0      
        i = 0
        n = len(prices)

        # Template to find localMin and localMax in an array
        while i < n-1:
            # Find local min
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            localMin = i

            # Find local max
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            localMax = i

            # Take profit
            profit += (prices[localMax] - prices[localMin])

        return profit

    # Accumulate Profit solution
    # Key insight: we can simply just keep selling while the price goes up.
    # This way we accumulate the same profit and avoid some condition checks required for computing local minima and maxima.
    def maxProfitOptimized(self, prices: List[int]) -> int:
        profit = 0

        for i in range (1, len(prices)):
            # Keep taking profit while the price goes up, because technically we can sell and buy again right away on the same day
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        
        return profit


    # -------------------------------------------------------------------------
    # Leetcode 845. Longest Mountain in Array
    def longestMountain(self, arr: List[int]) -> int:
        # start both pointer at 0
        i, j = 0, 0
        longest = 0
        
        # only go into while loop when i < len(arr) - 2 because 
        # a mountain has to have a length of at least 3
        while i < len(arr) - 2:
            # a earliest mountain can only start when arr[i] < arr[i+1] 
            while i < len(arr) - 1 and arr[i] >= arr[i+1]: 
                i += 1
                j += 1
            
            # find the left side of mountain
            while i < len(arr) - 1 and arr[i] < arr[i+1]:
                i += 1
            
            # now find the right side of the mountain
            # however, there are many possibilities can happen
            
            # account for when there is only 1 side of the mountain 
            if i == len(arr) - 1: break # end of array
            elif arr[i] == arr[i+1]: # not a mountain
                i += 1
                j = i
            else: # else it's a mountain
                while i < len(arr) - 1 and arr[i] > arr[i+1]:
                    i += 1
                longest = max(longest, i - j + 1)
                # set i and j back together
                j = i

        return longest


    # -------------------------------------------------------------------------
    # Leetcode 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        minDist = float("INF")
        criticalPoints = set()
        criticalPoint = 0
        
        # head cannot be a critical point
        prev = head
        current = head.next
        index = 1

        # Check directly if current is a critical point. Don't use the finding localMin and localMax template in this case
        while current and current.next:
            if (prev.val < current.val and current.val > current.next.val) or (prev.val > current.val and current.val < current.next.val):
                if criticalPoint != 0:
                    minDist = min( minDist, abs(index - criticalPoint) )
                criticalPoint = index
                criticalPoints.add(index)

            prev = current
            current = current.next
            index += 1

        print(criticalPoints)
        if len(criticalPoints) > 1:
            maxDist = max(criticalPoints) - min(criticalPoints)
            return [minDist, maxDist]
        
        return [-1,-1]


    # -------------------------------------------------------------------------
    # Leetcode 162. Find Peak Element
    # The reason why binary search works for this question is because it's guaranteed that a peak exists in the array
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (right+left) // 2
            # peak is on the right side
            if mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                left = mid + 1
                continue
            # peak is on the left side (including mid)
            if mid-1 >= 0 and nums[mid-1] > nums[mid]:
                right = mid
                continue

            # Retrun early: if both if statement above is not satisfied, then mid is a peak
            return mid

        return left


    # Leetcode 1276. Number of Burgers with No Waste of Ingredients
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        '''
        x = jumbo burger, y = small burger
        4x + 2y = tomatoSlices
        x + y = cheeseSlides  <=>  4x + 4y = 4cheeseSlides
        '''

        '''
        jumbo = (4*cheeseSlices - tomatoSlices) / 2
        small = cheeseSlices - jumbo

        if jumbo.is_integer():
            return [int(jumbo), int(small)]

        return []
        '''

        # use tomatoSlides to find cheeseSlides
        # binary search

        i = 0
        j = cheeseSlices

        while i <= j:
            y = (i + j) // 2 # number of small burger
            x = cheeseSlices - y # number of jumbo burger

            if 4 * x + 2 * y < tomatoSlices:
                # we want to increase the tomatoSlides -> increase jumbo -> decrase small
                # because x + y = cheese --> one more small means one less jumbo
                j = y - 1
            elif 4 * x + 2 * y > tomatoSlices:
                # we want to decrease tomatoSlides
                i = y + 1
            else: 
                return [x, y]
            
        return []


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
    # Leetcode 55 Jump Game
    # Use the idea of DP: "how-many-way" problem. But the code follow greedy algorithm
    # Let's say the targetLine is at the last index (len(nums)-1). We can greedily move the targetLine to the 0-th index
    def canJump(self, nums: List[int]) -> bool:
        targetLine = len(nums)-1

        # This way we only have to loop through nums one time --> O(n)
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= targetLine:
                targetLine = i

        return True if targetLine == 0 else False

    # -------------------------------------------------------------------------
    # Leetcode 45 Jump Game II
    #         0,1,2,3,4
    # nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    # Think of this as a graph problem where you can solve using BFS
    # Layer 0: index 0
    # Layer 1: index 1,2 (because from index 0, we can travel to all spot index 1->2)
    # Layer 2: index 3,4 (from any index in layer 1, we can travel furthest up to index 4)
    def jump(self, nums: List[int]) -> int:
        left = right = 0        # the window [left:right+1] will be the layer being examined
        jump = 0                # number of jump
        furthest = 0            # record the end of the next layer

        # -1 because we don't need to jump anymore at the last index
        while right < len(nums)-1: # and left <= right:      
            # Examine each index in this layer, just like BFS
            for i in range(left, right+1):
                furthest = max(furthest, i+nums[i])
            
            left = right + 1
            right = furthest
            jump += 1

        return jump # if left <= right else -1 (this leetcode question is guaranteed to have at leaset 1 solution)      

    # -------------------------------------------------------------------------
    # Leetcode 135. Candy
    def candy(self, ratings: List[int]) -> int:
        # Make use of two additional array: L and R
        n = len(ratings)
        left = [1] * n
        right = [1] * n

        # For L array, we traverse rating from left-> right. If rating[i] > rating[i-1] then L[i] = L[i+1]
        for L in range (1, n):
            if ratings[L] > ratings[L-1]:
                left[L] = left[L-1] + 1

        # Opposite for R array
        for R in range (n-1, 0, -1):
            if ratings[R-1] > ratings[R]:
                right[R-1] = right[R] + 1

        # Final candy distributed to each person will be max(L[i], R[i])
        candy = [1] * n
        for i in range (len(candy)):
            candy[i] = max(left[i], right[i])

        print(candy)
        return sum(candy)





if __name__ == "__main__":
    leetcode = Solution()

    # --------------------------------------------------------------------
    # costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    # mincost = leetcode.twoCitySchedCost(costs)
    # print("\nMin cost: ", mincost)

    # --------------------------------------------------------------------
    # nums = [1,2,1,3,5,6,4]
    # print(leetcode.findPeakElement(nums))

    # ----------------------------------- 55 -----------------------------------
    # nums = [3,2,1,0,4]
    # leetcode.canJump(nums)

    # ----------------------------------- 45 -----------------------------------
    nums = [3,2,1,0,4]
    print(leetcode.jump(nums))









