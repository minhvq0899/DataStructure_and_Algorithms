"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================== Two Pointers Exercise ==============================================

Leetcode 209. Minimum Size Subarray Sumv
Leetcode 560. Subarray Sum Equals K  <-- medium version of 209 
Leetcode 1234: Replace the Substring for Balanced String 
Leetcode 845. Longest Mountain in Array
Leetcode 3. Longest Substring Without Repeating Characters 
Leetcode 438. Find All Anagrams in a String
Leetcode 27. Remove Element
Leetcode 26. Remove Duplicates from Sorted Array
Leetcode 487. Max Consecutive Ones II
Leetcode 1004. Max Consecutive Ones III

# -----------------------------------------------------------------------------------------------
(Hard)
Leetcode 76. Minimum Window Substring

"""

from typing import List
from collections import defaultdict, Counter


class Solution:
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
    # Leetcode 560. Subarray Sum Equals K
    # Hard Medium: integers in nums can be negative
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_variable, count, i = 0, 0, 0
        accumulated_sum_dict = defaultdict(int) # dict contains how many time a sum has been recorded before
        
        while i < len(nums):
            sum_variable += nums[i]

            if sum_variable == k: # basic case
                count += 1
            if (sum_variable - k) in accumulated_sum_dict: # if sum != k, then we are checking in the dict to see if there has been a sum2 before where sum - k == sum2
                count += accumulated_sum_dict[sum_variable - k]
            
            accumulated_sum_dict[sum_variable] += 1
            i += 1

        return count
    
    
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
            # decrease the frequency of that char by 1  
            counter[code[s[R]]] -= 1
            # find the shortest substring
            while L < N and counter[0] <= n and counter[1] <= n and counter[2] <= n and counter[3] <= n:
                ans = min(ans, R-L+1)
                counter[code[s[L]]] += 1
                L += 1
            
        return ans


    # -----------------------------------------------------------------------------------------------
    # Leetcode 845. Longest Mountain in Array
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
    # Leetcode 27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers
        i = 0   # slow
        for j in range (len(nums)): # fast
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


    # -----------------------------------------------------------------------------------------------
    # Leetcode 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
        # same idea as Leetcode 27
        i = 0
        for j in range (len(nums)):
            if j == len(nums)-1 or nums[j] != nums[j+1]:
                nums[i] = nums[j]
                i += 1
        return i
    

    # -----------------------------------------------------------------------------------------------
    # Leetcode 487. Max Consecutive Ones II - similar to 1004 below, only diff is that K = 1
    # Leetcode 1004. Max Consecutive Ones III
    def longestOnes(self, nums: List[int], K: int) -> int:
        """
        Dem so luong 0 trong mang con hien va so sanh voi K
        Neu so luong so 0 ma nho hon K:
            Ta cu tang i 
        Neu so luong so 0 lon hon K
            Ta cu tang j
        """
        
        i, j = 0, 0
        counter = [0, 0] # counter number of 0s and 1s in substring
        final = 0
        nums.append(0)
        while i < len(nums):
            if counter[0] <= K: # if the number of 0 is still less than K
                # longest 1s will be the sum of 0 turned into 1 and actual 1s
                final = max(counter[0] + counter[1], final)
                # increase count of A[i]
                counter[nums[i]] += 1
                i += 1
            else:
                counter[nums[j]] -= 1 # decrase count of A[j]
                j += 1
        
        return final

        # ------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------
    # Leetcode 76. Minimum Window Substring
    def minWindow(self, s: str, t: str) -> str:
        # Create necessary DS
        counterS = Counter()                # not initialized yet
        counterT = Counter(t)
        need = len(counterT)
        have = 0

        # Initialize two pointers
        i, j = 0, 0
        minLen = float("INF")   
        resultI, resultJ = -1, -1   

        # Iterate through s using a for loop
        for j in range (len(s)):            
            charj = s[j]
            counterS[charj] += 1
            # check if including charj satisfy one more 'have'
            if counterS[charj] == counterT[charj]:
                have += 1
                # keep incrementing i while 'have' == 'need'
                while have == need:
                    # only update result if it's a better result
                    if j-i+1 < minLen:
                        minLen = j-i+1
                        resultI = i
                        resultJ = j

                    # update 'have' first, increment i, and remove s[i] from counterS
                    chari = s[i]
                    if counterS[chari] == counterT[chari]:
                        have -= 1                    
                    i += 1
                    counterS[chari] -= 1

        return s[resultI:resultJ+1]




if __name__ == "__main__":
    solution = Solution()
    
    # -------------------- Leetcode 560 --------------------
    nums = [3, 4, -7, 1, 3, 3, 1, -4]
    k = 7
    print('Answer for 560 is: ', solution.subarraySum(nums, k))

    # -------------------- Leetcode 1234 --------------------
    # print('Answer is: ', solution.balancedString('EQRWQQQW'))
                
    # -------------------- Leetcode 438 --------------------
    # s = "cbaebabacd"
    # p = "abc"
    # print(solution.findAnagrams(s, p))

    # -------------------- Leetcode 1004 --------------------
    # nums = [0,0,1,1,0,0,1]
    # print(solution.longestOnes(nums, 3))

    # --------------------------- 76 ---------------------------
    # s = "a"
    # t = "aa"
    # print( solution.minWindow(s,t) )

