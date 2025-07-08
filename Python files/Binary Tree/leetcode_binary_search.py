"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Search  =========================================================
(Easy)
Leetcode 35. Search Insert Position

(Medium)
Leetcode 875. Koko Eating Bananas
Leetcode 1011. Capacity To Ship Packages Within D Days

(Hard)
Leetcode 2468. Split Message Based on Limit (Hard) - Not a working solution, only pass 86/94 test cases

"""

from typing import List, Tuple


class Solution:
    # ------------------------------------------------------------------------------
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

    # ------------------------------------------------------------------------------
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

    # ------------------------------------------------------------------------------
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

    # ------------------------------------------------------------------------------
    # Leetcode 2468. Split Message Based on Limit (Hard) - Not a working solution, only pass 86/94 test cases
    def splitMessage(self, message: str, limit: int) -> List[str]:
        if limit <= 5: return []
        
        # notice: the max # of parts the message can be splitted into is len(message), and the min is 1
        # do a binary search to find the exact # of parts
        L = 1
        R = len(message)
        solution = 0

        while L < R:
            mid = L + (R - L) // 2
            possible, foundSolution = self.helperSplit(message, limit, mid)

            if foundSolution: 
                solution = mid
                break

            # case 1: it's possible to split message to 'mid' number of part -> we can do better
            if possible:
                R = mid - 1
            # case 2: it's not possible -> we need to split to more parts
            else: 
                L = mid + 1
        
        if L == R: 
            possible, foundSolution = self.helperSplit(message, limit, L)
            if foundSolution: solution = L
            else: return []
        
        # Compute the answer list to return
        partList = self.computePartsList(message, limit, solution)

        return partList
        
    def helperSplit(self, message: str, limit: int, numOfPart: int) -> [bool, bool]:
        numDigitOfNumPart = len(str(numOfPart))
        n = len(message)
        i = 1
        partCounter = 1
        
        # i is the # digit of # of parts, starting from 1
        while i <= numDigitOfNumPart and n > 0: 
            numDigitOfEachPart = limit - 3 - numDigitOfNumPart - i
            # here we will count from smallest number with i digit to the largest number with i digit
            # eg. if i == 2, we will count from 10 -> 99
            # startCount = 10**(i - 1) if i > 1 else 0
            endCount = 10**i
            while partCounter < endCount and n > 0:
                n -= numDigitOfEachPart
                partCounter += 1

            # Case 1: It's not possible (we need more number of parts)
            if partCounter-1 > numOfPart:
                break

            i += 1
        
        # Case 2: It's possible, and we found the solution
        if partCounter-1 == numOfPart and n <= 0:
            return [True, True]
            
        # Case 3: It's possible, but it's not the soluton we are looking for
        if partCounter-1 < numOfPart:
            return [True, False]

        return [False, False]

    def computePartsList(self, message: str, limit, numOfPart: int) -> List[str]:
        numDigitOfNumPart = len(str(numOfPart))
        i = 1               # i is the # digit of # of parts, starting from 1
        partsList = []
        suffixFormat = "<{}/" + str(numOfPart) + ">"
        partCounter = 1
        
        while i <= numDigitOfNumPart and len(message) > 0: 
            # here we will count from smallest number with i digit to the largest number with i digit
            # eg. if i == 2, we will count from 10 -> 99
            # startCount = 10**(i - 1) if i > 1 else 0
            endCount = 10**i
            while partCounter < endCount and len(message) > 0: 
                suffix = suffixFormat.format(partCounter)
                numDigitOfEachPart = limit - len(suffix)
                strPart = message[ 0:numDigitOfEachPart ]
                message = message[ numDigitOfEachPart:]
                part = strPart + suffix
                partsList.append(part)
                partCounter += 1

            i += 1
            
        return partsList






if __name__ == "__main__":
    leetcode = Solution()

    # ---------------------- 35 ----------------------
    # idx = leetcode.searchInsert( [1,3,5,6], 2 )
    # print(idx)

    # ---------------------- 1011 ----------------------
    # print( "Final: ", leetcode.shipWithinDays_test( [3,2,2,4,1,4], 3 ) )

    # ---------------------- 875 ----------------------
    # print( "Final: ", leetcode.minEatingSpeed( [312884470], 312884469 ) )

    # ---------------------- 2468 ----------------------
    message = "abbababbbaaa aabaa a"
    limit = 8
    print( leetcode.splitMessage(message, limit) )
