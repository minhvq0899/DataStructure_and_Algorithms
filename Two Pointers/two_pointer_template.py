"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================== Two Pointers Exercise ==============================================
1. Leetcode 560. Subarray Sum Equals K
2. Leetcode 1234: Replace the Substring for Balanced String
3. Leetcode 845. Longest Mountain in Array
4. Leetcode 209. Minimum Size Subarray Sum
5. Leetcode 3. Longest Substring Without Repeating Characters
6. Leetcode 438. Find All Anagrams in a String
7. Leetcode 27. Remove Element
8. Leetcode 26. Remove Duplicates from Sorted Array

"""

from typing import List


# Leetcode 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
# Using two pointers, we can reduce from O(n^2) down to O(n)

# 1. Easy: all integers in nums are positive
# 2. Medium: integers in nums can be negative
class subarraySumEqualsK:
    # [1,2,6,3,5,1,8,9] with K = 9
    def easy(self, nums: List[int], K: int) -> int:
        i, j = 0, 0
        sum = 0
        cnt = 0 # counts of subarray
        while i < len(nums): 
            if sum + nums[i] < K:
                sum += nums[i]
                i += 1
            elif sum + nums[i] > K:
                sum -= nums[j]
                j += 1
            else: # this covers for when sum + nums[i] == K  --> we found another subarray
                cnt += 1
                sum += nums[i]
                i += 1
            
        return cnt

    def medium(self, nums: List[int], K: int) -> int:
        pass




class Solution:
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


    # ==============================================================================================
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


    # ==============================================================================================
    # Leetcode 209. Minimum Size Subarray Sum
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')              # global var to store answer
        sum = 0                             # global var to store current sum
        left = 0                            # right pointer

        for right in range (len(nums)):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0



    # ==============================================================================================
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


    # ==============================================================================================
    # Leetcode 438. Find All Anagrams in a String
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # basic check
        if len(s) < len(p): return []

        ans = []                        # a list to store answers

        chars = [0 for _ in range (26)] # an array represents how many of each char to do we need to make an anagram
        for i in range (len(p)):        # populate the array
            slot = ord(p[i]) - 97
            chars[slot] += 1

        diff = len(p)                   # the distance between window and p
        first_window = s[:len(p)]
        for i in range (len(first_window)):
            slot = ord(first_window[i]) - 97
            chars[slot] -= 1
            if chars[slot] >= 0: diff -= 1          # if chars[slot] is positive, the char is in p

        # sliding window part: fixed window size
        for left in range (len(s) - len(p) + 1):
            # validate the window on the fly
            if left: # if left != 0
                right = left + len(p) - 1
                left_char = s[left - 1]
                right_char = s[right]

                chars[ord(left_char) - 97] += 1                 # the prev char is out of the window
                if chars[ord(left_char) - 97] > 0: diff += 1

                chars[ord(right_char) - 97] -= 1                # the new char is added to the window
                if chars[ord(right_char) - 97]  >= 0: diff -= 1

            print(diff)
            if diff == 0:               # found an anagram
                ans.append(left)
                
        return ans


    # ==============================================================================================
    # Leetcode 27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers
        i = 0   # slow
        for j in range (len(nums)): # fast
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

     

    # ==============================================================================================
    # Leetcode 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
        # same idea as Leetcode 27
        i = 0
        for j in range (len(nums)):
            if j == len(nums)-1 or nums[j] != nums[j+1]:
                nums[i] = nums[j]
                i += 1
        return i
    




if __name__ == "__main__":
    solution = Solution()
    
    # print('Answer is: ', solution.balancedString('EQRWQQQW'))
                
    s = "abab"
    p = "ab"
    print(solution.findAnagrams(s, p))


