"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================== Two Pointers Exercise ==============================================
(Template for Count Subarrays with At Most K Feature)
countSubarraysAtMostK() - Counting Subarrays (e.g. with at most K features)
    992, 1248
    2962. Count Subarrays Where Max Element Appears at Least K Times
        Total number of non-empty subarray: n*(n+1)//2
        Total number of subarray, including empty subarray: n*(n+1)//2 + 1 (simply including the one empty subarray)
longestValidSubarray() - Maximum Length Subarray (longest valid subarray)
    304, 567
    Leetcode 904. Fruit Into Baskets
countSubarraysWithSumK() - Subarray Sum Constraints (e.g. sum == K) 
    560, 930, 974

# -----------------------------------------------------------------------------------------------
(Easy)
    Leetcode 27. Remove Element
    Leetcode 26. Remove Duplicates from Sorted Array

# -----------------------------------------------------------------------------------------------
(Medium)
    [Basic] Leetcode 11. Container With Most Water
    [Basic] Leetcode 209. Minimum Size Subarray Sum
    [Basic + flipping char] Leetcode 1234: Replace the Substring for Balanced String 
    [Basic] Leetcode 3. Longest Substring Without Repeating Characters 
    [Keep comparing two Counter objects] Leetcode 438. Find All Anagrams in a String
    [Flipping char/int] Leetcode 487. Max Consecutive Ones II
    [Flipping char/int] Leetcode 1004. Max Consecutive Ones III
    [k-at-most template] Leetcode 1248. Count Number of Nice Subarrays
    Leetcode 658. Find K Closest Elements

# -----------------------------------------------------------------------------------------------
(Hard)
    [Keep comparing two Counter objects] Leetcode 76. Minimum Window Substring
    Leetcode 42. Trapping Rain Water
    [k-at-most template] Leetcode 992. Subarrays with K Different Integers

"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    # Counting Subarrays (e.g. with at most K features)
    def countSubarraysAtMostK(nums, k, is_valid):
        count = 0
        left = 0
        freq = {}

        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1

            while not is_valid(freq, k):
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1

        return count

    # Maximum Length Subarray (longest valid subarray)
    def longestValidSubarray(nums, k, is_valid):
        left = 0
        max_len = 0
        freq = {}

        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1

            while not is_valid(freq, k):
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
    # Subarray Sum Constraints (e.g. sum == K) 
    # 🔧 Prefix Sum Variant Templat
    def countSubarraysWithSumK(nums, k):
        prefix_sum = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - k]
            freq[prefix_sum] += 1

        return count

    # ===============================================================================================
    # Leetcode 27. Remove Element (Easy)
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers
        i = 0   # slow
        for j in range (len(nums)): # fast
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    # -----------------------------------------------------------------------------------------------
    # Leetcode 26. Remove Duplicates from Sorted Array (Easy)
    def removeDuplicates(self, nums: List[int]) -> int:
        # same idea as Leetcode 27
        i = 0
        for j in range (len(nums)):
            if j == len(nums)-1 or nums[j] != nums[j+1]:
                nums[i] = nums[j]
                i += 1
        return i
    
    
    # ===============================================================================================
    # Leetcode 11. Container With Most Water
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxWater = min(height[left], height[right]) * (right-left)

        # Keep moving the lower bar
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            maxWater = max(maxWater, min(height[left], height[right]) * (right-left))

        return maxWater

    # -----------------------------------------------------------------------------------------------
    # Leetcode 209. Minimum Size Subarray Sum
    # Easy Medium: all integers in nums are positive
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')              # global var to store answer
        sum = 0                             # global var to store current sum
        left = 0                            # right pointer

        # basic approach
        for right in range (len(nums)):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0
    
   
    # -----------------------------------------------------------------------------------------------
    # Leetcode 1234: Replace the Substring for Balanced String
    def balancedString(self, s: str) -> int:
        N = len(s) # length of s
        n = N/4 # maximum number of apperance for each letter
        
        # make a dict so we can refer to each leter easier
        code = {'Q': 0, 'W': 1, 'E': 2, 'R': 3}
        # counter of each letter: Q, W, E, R
        counter = [0] * 4
        # first, count each letter
        for char in s:
            counter[code[char]] += 1
        
        # Return 0 if the string is already balanced
        if counter[0] == counter[1] == counter[2] == counter[3]:
            return 0
        
        # start at 0
        # keep counts of the amount of characters outside of 2-pointers range are
        # smaller or equal to n/4
        L = 0
        ans = N
        for R in range (N):
            # decrease the frequency of charR by 1 before moving R
            counter[code[s[R]]] -= 1
            # find the shortest substring
            while L < N and counter[0] <= n and counter[1] <= n and counter[2] <= n and counter[3] <= n:
                ans = min(ans, R-L+1)
                # increase the frequency of charL by 1 before moving L 
                counter[code[s[L]]] += 1
                L += 1
            
        return ans

    # -----------------------------------------------------------------------------------------------
    # Leetcode 3. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seenset = set()
        left = 0

        for right in range (len(s)):
            # remove left until you find the previous occurrence of s[right]
            while s[right] in seenset: 
                seenset.remove[s[left]]
                left += 1
            # add char at right in set
            seenset.add(s[right])
            # store result
            max_len = max(max_len, right - left + 1)
        
        return max_len


    # -----------------------------------------------------------------------------------------------
    # Leetcode 438. Find All Anagrams in a String
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []

        # Track character frequencies in p and window
        target_freq = Counter(p)  
        window_freq = Counter()

        # populate the first window freq
        L, R = 0, 0
        while R < L + len(p):
            window_freq[s[R]] += 1
            R += 1
        R -= 1

        ans = []
        # Compare window frequencies with target frequencies
        if window_freq == target_freq:
            ans.append(L)

        while R < len(s)-1:
            # move the window
            if window_freq[s[L]] == 1:
                del window_freq[s[L]]  # Remove fully
            else:
                window_freq[s[L]] -= 1  # Decrease count
            L += 1

            R += 1
            window_freq[s[R]] += 1  # Increase count

            # Compare window frequencies with target frequencies
            if window_freq == target_freq:
                ans.append(L)

        return ans


    # -----------------------------------------------------------------------------------------------
    # Leetcode 487. Max Consecutive Ones II - similar to 1004 below, only diff is that K = 1
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = [0, 0]            # keep count of 0s and 1s in the sliding window
        maxLen = 0
        R, L = 0, 0

        # We need to append a 0 in the end before the while loop because we compute the maxLen BEFORE incrementing R
        nums.append(0)              
        while R < len(nums):
            # Only compute the maxLen if number of 0s is smaller than or equals to K (1 in this case)
            if counter[0] <= 1:
                # Keep incrementing R and computing the max len
                maxLen = max(maxLen, counter[0] + counter[1])
                counter[nums[R]] += 1   
                R += 1
            # If number of 0s is more than 1 now, we need to increment L
            else:
                counter[nums[L]] -= 1
                L += 1
        
        print(maxLen)
        return maxLen

    # -----------------------------------------------------------------------------------------------
    # Leetcode 1004. Max Consecutive Ones III
    def longestOnes(self, nums: List[int], K: int) -> int:
        """
        Dem so luong 0 trong mang con hien va so sanh voi K
        Neu so luong so 0 ma nho hon K:
            Ta cu tang i 
        Neu so luong so 0 lon hon K
            Ta cu tang j
        """
        L, R = 0, 0
        counter = [0, 0] # counter number of 0s and 1s IN SUBSTRING
        final = 0
        nums.append(0)
        while R < len(nums):
            # if the number of 0 is still less than K
            if counter[0] <= K: 
                # longest 1s will be the sum of 0 turned into 1 and actual 1s
                final = max(counter[0] + counter[1], final)
                # increase count of A[i]
                counter[nums[R]] += 1
                R += 1
            else:
                # decrase count of A[j]
                counter[nums[L]] -= 1 
                L += 1
        
        return final


    # -----------------------------------------------------------------------------------------------
    # Leetcode 1248. Count Number of Nice Subarrays
    # Solution 1: exactly_k = at_most_k - at_most_(k - 1)
    def numberOfSubarrays1(self, nums: List[int], k: int) -> int:
        # Helper function: count subarrays with at most k odd numbers ---------
        def at_most(k: int) -> int:
            left = 0
            count = 0
            odd_count = 0

            for right in range(len(nums)):
                # If current number is odd, increment odd_count
                if nums[right] % 2 == 1:
                    odd_count += 1

                # Shrink window from the left if odd_count exceeds k
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                # All subarrays ending at right and starting from left to right are valid
                count += right - left + 1

            return count
        # ------------------------------------------------------------------------

        # Subarrays with exactly k odd numbers = at_most(k) - at_most(k - 1)
        return at_most(k) - at_most(k - 1)

    
    # -----------------------------------------------------------------------------------------------
    # Leetcode 2962. Count Subarrays Where Max Element Appears at Least K Times
    # answer = (total number of non-empty subarray) - at_most(k-1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Helper fn to count number of subarray with at most K feature (in this case, feature is the max element appears K times)
        # --------------------------------------------------------
        def numSubarrayAtMostKTime(k) -> int:
            freq = 0
            left = 0
            count = 0
            maxElement = max(nums)

            for right in range(len(nums)):
                if nums[right] == maxElement:
                    freq += 1
                
                # Shrink the window
                while freq > k:
                    if nums[left] == maxElement:
                        freq -= 1
                    left += 1

                count += (right-left+1)

            return count
        # --------------------------------------------------------
        n = len(nums)
        totalSubarray = n * (n+1) // 2

        # answer = (total number of non-empty subarray) - at_most(k-1)
        return totalSubarray - numSubarrayAtMostKTime(k-1)

    # -----------------------------------------------------------------------------------------------
    # Leetcode 904. Fruit Into Baskets
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxLen = 0
        counter = {}

        for right, rightVal in enumerate(fruits):
            counter[rightVal] = counter.get(rightVal, 0) + 1

            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1
            
            maxLen = max(maxLen, (right-left+1))

        return maxLen


    # -----------------------------------------------------------------------------------------------
    # Leetcode 658. Find K Closest Elements
    # Helper fn that returns True if a is closer to x than b
    def closer(self, a: int, b: int, x: int) -> bool:
        diffA = abs(a - x)
        diffB = abs(b - x)

        if diffA < diffB: 
            return True
        elif diffA > diffB:
            return False
        else:
            if a < b: 
                return True
            else: 
                return False

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Corner case: X is not in range [arr[0], arr[-1]]
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[len(arr)-k:]
        
        # If X is within range [arr[0], arr[-1]]
        left, right = 0, len(arr) - 1
        while (right - left + 1) > k:       # while the len of window is bigger than k
            # if element at left is closer to X than element at right -> move right down
            if self.closer(arr[left], arr[right], x):
                right -= 1
            else:
                left += 1
        
        return arr[left : right + 1]


    # =================================================================================================
    # -----------------------------------------------------------------------------------------------
    # Leetcode 76. Minimum Window Substring
    def minWindow(self, s: str, t: str) -> str:
        # Create necessary DS
        counterS = Counter()                # not initialized yet
        counterT = Counter(t)
        need = len(counterT)
        have = 0

        # Initialize two pointers
        R, L = 0, 0
        minLen = float("INF")   
        resultL, resultR = -1, -1   

        # Iterate through s using a for loop
        for R in range (len(s)):            
            charR = s[R]
            counterS[charR] += 1
            # check if including charR satisfy one more 'have'
            if counterS[charR] == counterT[charR]:
                have += 1
                # keep incrementing i while 'have' == 'need'
                while have == need:
                    # only update result if it's a better result
                    if R-L+1 < minLen:
                        minLen = R-L+1
                        resultL = L
                        resultR = R

                    # update 'have' first, increment i, and remove s[i] from counterS
                    charL = s[L]
                    if counterS[charL] == counterT[charL]:
                        have -= 1                    
                    L += 1
                    counterS[charL] -= 1

        return s[resultL:resultR+1]

    # -----------------------------------------------------------------------------------------------
    # Leetcode 42. Trapping Rain Water
    """
    - Water trapped at index i is determined by: min(max_left[i], max_right[i]) - height[i]
    - Instead of precomputing max_left and max_right arrays (which takes O(n) space), we use two pointers and update max values on the fly.
    - Always move the pointer with the smaller max height, because that side limits the water level.
    """
    # This solution takes O(n) of space complexity
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right = [0 for _ in range (n)], [0 for _ in range (n)]

        # Initialize max_left and max_right array separately
        for L in range (1, n):
            max_left[L] = max(height[L-1], max_left[L-1])

        for R in range (n-2, -1, -1):
            max_right[R] = max(height[R+1], max_right[R+1])

        # print(max_left)
        # print(max_right)

        # Compute rainTrap array separately
        rainTrap = [0 for _ in range (n)]
        for i in range (n):
            rainTrap[i] = max( min(max_left[i], max_right[i]) - height[i] , 0 )

        print(rainTrap)
        return sum(rainTrap)
    
    # This solution takes O(1) of space complexity
    def trap2(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_L, max_R = 0, 0
        rain = 0

        # Since we only cares about the min between max_L and max_R, we don't have to precompute max_L and max_R beforehand. 
        # If max_L < local max_R, it will definitely be smaller the global max_R
        while L <= R:
            if max_L < max_R:
                rain += max( max_L - height[L], 0 )
                max_L = max(max_L, height[L])
                L += 1
            else:
                rain += max( max_R - height[R], 0 )
                max_R = max(max_R, height[R])
                R -= 1

        print(rain)
        return rain

    # -----------------------------------------------------------------------------------------------
    # Leetcode 992. Subarrays with K Different Integers
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Helper fn to count number of subarrays with AT MOST k distinct integers--------------
        def numSubArrayWithAtMostKInt(k) -> int:
            counter = {}
            left = 0
            count = 0

            # Sliding window template
            for right in range (len(nums)):
                numsRight = nums[right]
                # Increment the freq of char at right
                if numsRight not in counter:
                    counter[numsRight] = 1
                else:
                    counter[numsRight] += 1

                # Update the sliding window
                while len(counter) > k:
                    numsLeft = nums[left]
                    counter[numsLeft] -= 1
                    if counter[numsLeft] == 0:
                        del counter[numsLeft]

                    left += 1

                # print("right: {}, left: {}".format(right, left))
                count += (right-left+1)

            return count
        # -------------------------------------------------------------------------------------

        # print("k = {} -> {}".format(k, numSubArrayWithAtMostKInt(k)) )
        # print("k = {} -> {}".format(k-1, numSubArrayWithAtMostKInt(k-1)))
        return numSubArrayWithAtMostKInt(k) - numSubArrayWithAtMostKInt(k-1)





if __name__ == "__main__":
    solution = Solution()

    # -------------------- Leetcode 1234 --------------------
    # print('Answer is: ', solution.balancedString('EQRWQQQW'))
                
    # -------------------- Leetcode 438 --------------------
    # s = "cbaebabacd"
    # p = "abc"
    # print(solution.findAnagrams(s, p))

    # -------------------- Leetcode 487 --------------------
    # nums = [1,1,0,1]
    # solution.findMaxConsecutiveOnes(nums)

    # -------------------- Leetcode 1004 --------------------
    # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    # print(solution.longestOnes(nums, 3))

    # -------------------- Leetcode 1248 --------------------
    # nums  = [2,2,2,1,2,2,1,2,2,2]
    # solution.numberOfSubarrays1(nums, 2)

    # --------------------------- 76 ---------------------------
    # s = "a"
    # t = "aa"
    # print( solution.minWindow(s,t) )

    # --------------------------- 42 ---------------------------
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # solution.trap2(height)

    # --------------------------- 992 ---------------------------
    # nums = [1,2,1,3,4]
    # k = 3
    # print(solution.subarraysWithKDistinct(nums, k))

    # --------------------------- 2962 ---------------------------
    nums = [1,3,2,3,3]
    k = 2
    print(solution.countSubarrays(nums, k))

    