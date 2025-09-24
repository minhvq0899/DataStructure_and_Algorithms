"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Search  =========================================================
(Easy)
Leetcode 35. Search Insert Position

(Medium)
    (Monotonic function within the list)
Leetcode 153. Find Minimum in Rotated Sorted Array
Leetcode 33. Search in Rotated Sorted Array
    (Checking possibility of mid)
Leetcode 875. Koko Eating Bananas
Leetcode 1011. Capacity To Ship Packages Within D Days
Leetcode 1482. Minimum Number of Days to Make m Bouquets

(Hard)
Leetcode 2468. Split Message Based on Limit (Hard) - Not a working solution, only pass 86/94 test cases
Leetcode 2071. Maximum Number of Tasks You Can Assign
Leetcode 4. Median of Two Sorted Arrays
Leetcode 410. Split Array Largest Sum - same pattern of using isPossible() helper

"""

from typing import List, Tuple
import bisect


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


    # ==============================================================================
    # ------------------------------------------------------------------------------
    # Leetcode 153. Find Minimum in Rotated Sorted Array
    def findMin(self, nums: List[int]) -> int:
        # Monotonic relation of these elements: <= nums[-1]
        L, R = 0, len(nums) - 1

        while L <= R: 
            mid = (R + L) // 2
            
            # case 1: min element is next to mid to the right
            if mid+1 < len(nums) and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            # case 2: min element is mid
            if mid-1 >= 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            # look to the left
            if nums[mid] <= nums[-1]:
                R = mid - 1
            # look to the right
            else:
                L = mid + 1

        return nums[mid]


    # ------------------------------------------------------------------------------
    # Leetcode 33. Search in Rotated Sorted Array
    def search(self, nums: List[int], target: int) -> int:
        # pivot will be nums[-1]
        # binary search
        L, R = 0, len(nums)-1
        while L <= R:
            mid = (R + L) // 2
            
            # Found it
            if nums[mid] == target:
                return mid
            
            # Case 1: Left halve is sorted
            if nums[L] <= nums[mid]:
                # If target belongs to the sorted halve -> look to the left
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else: 
                    L = mid + 1
            # Case 2: Right halve is sorted
            else:
                # If target belongs to the sorted halve -> look to the right
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else: 
                    R = mid - 1
                
        return -1


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
    # Leetcode 1482. Minimum Number of Days to Make m Bouquets
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)
        
        # ------------------------------------------
        def isPossible(days: int):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

                if bouquets >= m:
                    return True

            return False
        # ------------------------------------------

        ans = -1
        while left <= right:
            mid = (right+left) // 2
            if isPossible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans



    # ==============================================================================
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
    
    # ------------------------------------------------------------------------------
    # Leetcode 2071. Maximum Number of Tasks You Can Assign
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # Sort the two inputs
        tasks.sort()
        workers.sort()

        # ---------------------------------------------------------
        def isPossible(k: int, numPills: int) -> bool:
            # Deque that contains k strongest workers, in increasing order
            k_strongest_workers = workers[-k:]
            # Array contains k easiest tasks, in increasing order
            k_easiest_tasks = tasks[:k]

            # Assign the task from hardest -> easiest
            for i in range (len(k_easiest_tasks)-1, -1, -1):
                task = k_easiest_tasks[i]

                # Check if each task can be completed by a worker
                # Case 1: current strongest worker can complete this task
                if k_strongest_workers[-1] >= task:
                    k_strongest_workers.pop()
                # Case 2: we look for the minimum worker with value ≥ t−strength
                elif numPills > 0:
                    workerIndex = bisect.bisect_left(k_strongest_workers, (task-strength), 0, len(k_strongest_workers))
                    if workerIndex != len(k_strongest_workers):
                        k_strongest_workers.remove(k_strongest_workers[workerIndex])
                        numPills -= 1
                    else:
                        return False
                # Case 3: It's impossible to complete k hardest tasks with k strongest workers
                else:
                    return False

            return True
        
        # ---------------------------------------------------------

        # Binary search to find k number of tasks can be completed 
        left, right = 0, min( len(tasks), len(workers) )
        ans = 0
        while left <= right:
            mid = (right+left) // 2
            if isPossible(mid, pills):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans

    # ------------------------------------------------------------------------------
    # Leetcode 4. Median of Two Sorted Arrays   ( O(log(m+n)) because we are doing binary search on the shorter array to find the right 'mid1')
    #          0 1 2 3 4 5 6 7
    # nums2 = [1,2,3,4,5,6,7,8]     -> left2 = 4, right2 = 5
    #          0 1 2 3 
    # nums1 = [1,2,3,4]             -> left1 = 2, right1 = 3
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Idea: In the example above, if we merge two arrays together, we will have one big array size 12
        # The median will be the average of 5th and 6th element, which divide our total array into 2 equal partitions (each of size 6)
        # The left partition of the total array is made up of the left partition of nums1 and left partition of nums2
        # On each search, we need to find the correct 'midTemp1' and 'midTemp2' to correctly split our two arrays, so that both of their left partitions, when 
        # put together, correctly make up the correct left partition of our total array
        total = len(nums1) + len(nums2)
        half = total // 2

        # Making sure that temp1 will always be the shorter array
        temp1, temp2 = nums1, nums2
        if len(temp1) > len(temp2):
            temp1, temp2 = nums2, nums1

        # Binary search: always start with the shorter array
        left, right = 0, len(temp1)-1
        while True:
            midTemp1 = (left + right) // 2
            midTemp2 = half - midTemp1 - 2      # -2 to account for array index starting from 0

            # After choosing the 'mid' for both temp arrays, we now have to validate if those two mids are correct
            # 'left' will be either the element to the left of that array median or the mid element
            # 'right' will be the element to the right of that array median
            left1 = temp1[midTemp1] if midTemp1 >= 0 else float('-inf')
            right1 = temp1[midTemp1+1] if midTemp1+1 < len(temp1) else float('inf')
            left2 = temp2[midTemp2] if midTemp2 >= 0 else float('-inf')
            right2 = temp2[midTemp2+1] if midTemp2+1 < len(temp2) else float('inf')

            # Validate
            # Case 1: If we correctly found the two mids
            if left1 <= right2 and left2 <= right1:
                # Case 1.1: Total array has odd len -> median will be the min of 'left1' and 'left2'
                if total % 2 == 1:
                    return min(right1, right2)
                
                # Case 1.2: even len
                return ( max(left1, left2) + min(right1, right2) ) / 2
            # Case 2: We need more element from temp1 in our left partition
            elif left2 > right1:
                left = midTemp1 + 1
            # Case 3: We need less element from temp1 in our left partition    
            else:
                right = midTemp1 - 1

    
    # ------------------------------------------------------------------------------
    # Leetcode 410. Split Array Largest Sum
    # The minimum subarray sum is the largest element of the array (meaning each subarray has len 1)
    # The maximum subarray sum is the sum of the whole array
    # Therefore, we can do BS on the range of subarray sum. For each potential value, greedily check if we can split the array
    # in less than or equal to k subarrays so that sum of each subarray is <= potential value
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        # ----------------------------------------
        # For each potential value, greedily check if we can split the array
        # in less than or equal to k subarrays so that sum of each subarray is <= potential value
        def canSplit(maxSum: int) -> bool:
            subarrayCount = 1
            currentSum = 0

            for num in nums:
                if currentSum + num > maxSum:
                    subarrayCount += 1
                    currentSum = num
                    if subarrayCount > k:
                        return False
                else:
                    currentSum += num

            return True
        # ----------------------------------------

        # Do binary search to find the minimized sum
        answer = 0
        while left <= right:
            mid = (right+left) // 2
            if canSplit(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer






if __name__ == "__main__":
    leetcode = Solution()

    # ---------------------- 35 ----------------------
    # idx = leetcode.searchInsert( [1,3,5,6], 2 )
    # print(idx)

    # ---------------------- 153 ----------------------
    # nums = [4,5,6,7,0,1,2]
    # print(leetcode.findMin(nums))

    # ---------------------- 33 ----------------------
    # nums = [4,5,6,7,0,1,2]
    # print(leetcode.search(nums, 0))

    # ---------------------- 1011 ----------------------
    # print( "Final: ", leetcode.shipWithinDays_test( [3,2,2,4,1,4], 3 ) )

    # ---------------------- 875 ----------------------
    # print( "Final: ", leetcode.minEatingSpeed( [312884470], 312884469 ) )

    # ---------------------- 2468 ----------------------
    # message = "abbababbbaaa aabaa a"
    # limit = 8
    # print( leetcode.splitMessage(message, limit) )

    # ---------------------- 2071 ----------------------
    # tasks = [5181,2717,7678,7730,5931,8066,2266,5873,3645,6636,3308,2848,2082,7158,5398,4030,4942,1723,6614,5165,8086,7526,9503,2051,5305,6606,7514,5078,1149,5782,4717,5969,4966,1292,4370,3863,4111,1140,2980,5295,5347,8700,2833,6750,2352,7604,6305,2697,7501,7719,7955,7901,1779,6850,6456,1040,9230,2712,8129,9875,9385,1814,8167,2960,9191,3588,7339,2255,5314,2873,3294,5375,6745,5984,9717,4983,2558,8075,7988,6490,4499,7236,2097,8097,2923,2972,8609,8993,6354,6502,3340,1666,1281,9703,8869,5274,8150,5270,3437,3171,7423,5865,1995,7002,8550,9908,7114,8777,1250,5855,3501,9316,5380,3877]
    # workers = [2167,4646,1582,1102,2113,1258,4341,3193,3136,4096,3311,1501,3499,1815,1282,4914,772,4785,2632,1223,3479,3010,3505,1613,4257,1192,2918,2664,4274,4036,1039,1250,4713,3443,4514,4117,3400,3825,1782,3552,2386,865,2290,3618,793,1297,908,2187,3273,4531,3859,605,4274,3951,583,1135,2802,3585,727,2359,4011,4071,2035,4775,764,4702,2050,3304,3876,3772,4946,4371,1993,4746,1124,1221,1368,831,2337,506,951,3874,3094,2744,4258,4704,3229,1015,4876,1893,3098,4464,4189,4201,3986,3673,4126,2424,4280,2780,1748,1650,1591,753,3392,2498,835,608,1746,1243,3778,1382,4207,1909,832,4501,781,1274,973,4966,1873,2512,3644,3244,1120,4979,3945,1481,2172,4410,3572,4597,3414,4306,4714,4047,3239,4557,3226,3273,4997,3374]
    # pills = 139
    # strength = 2075
    # ans2071 = leetcode.maxTaskAssign(tasks, workers, pills, strength)
    # print(ans2071)

    # ---------------------- 4 ----------------------
    # nums1 = [1,2,3,4,5,6,7,8]
    # nums2 = [1,2,3,4]
    # leetcode.findMedianSortedArrays(nums1, nums2)

    # ---------------------- 410 ----------------------
    # nums = [1,2,3,4,5]
    # k = 4
    # answer410 = leetcode.splitArray(nums, k)
    # print(answer410)

    bloomDay = [7,7,7,7,12,7,7]
    ans1482 = leetcode.minDays(bloomDay, 2, 3)
    print(ans1482)

