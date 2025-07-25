"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================= Template for Dynamic Programming =========================================

(Easy)
Leetcode 263: Ugly Number

# ------------------------------------------------
(Medium)
Leetcode 70: Climbing Stairs
Leetcode 322. Coin Change
Leetcode 300. Longest Increasing Subsequence
Leetcode 139. Word Break

Leetcode 1143. Longest Common Subsequence
Leetcode 516. Longest Palindromic Subsequence
Leetcode 5. Longest Palindromic Substring
Leetcode 647. Palindromic Substrings
Classic 0/1 Knapsack Problem
   Similar idea: Leetcode 474. Ones and Zeroes
Leetcode 198. House Robber
Leetcode 213. House Robber II
Leetcode 337. House Robber III

Leetcode 53. Maximum Subarray
Leetcode 152: Maximum Product Subarray

# ------------------------------------------------
(Hard)    
Leetcode 10. Regular Expression Matching (Hard)
Leetcode 2472. Maximum Number of Non-overlapping Palindrome Substrings (Hard)

"""
import bisect
from typing import List, Tuple
from array import *
from collections import defaultdict
from functools import lru_cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # --------------------------------------------------------------------------------------------------
    # Leetcode 263: Ugly Number
    def nthUglyNumber(self, n: int) -> int:
        '''
        Any ugly number must be in one of these three sequence
        (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
        (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
        (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
        '''
        # initialize stored array
        ugly = [None] * n
        ugly[0] = 1
        
        # initialize 3 index pointers
        i2, i3, i5 = 0, 0, 0
        
        # Assume you have Uk, the kth ugly number. 
        # Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5), with L1, L2, L3 
        # be three of the previous ugly numbers (can be Uk+1)
        next_multiple_of_2 = ugly[i2] * 2
        next_multiple_of_3 = ugly[i3] * 3
        next_multiple_of_5 = ugly[i5] * 5
        
        # loop to that n-th ugly number we need
        for i in range (1, n):
            ugly[i] = min(next_multiple_of_2,
                          next_multiple_of_3,
                          next_multiple_of_5)
            # we prioritize i2, meaning if there is an ugly number can be
            # computed by two number (ex: 10 = 2*5 and 5*2), we prioritize 
            # increasing the small number (2)
            if ugly[i] == next_multiple_of_2: 
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            
            if ugly[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            
            if ugly[i] == next_multiple_of_5: 
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
        
        print(ugly)
        
        return ugly[-1]
    
    # --------------------------------------------------------------------------------------------------
    # leetcode 70: Climbing Stairs
    # -------- top down solution --------
    def climbStairs_top_down(self, n: int) -> int:
        # ----------------
        def memorization(n: int, memo: List[int]) -> int:
            if memo[n] == -1: 
                memo[n] = memorization(n-1, memo) + memorization(n-2, memo)
            return memo[n]
        # ----------------

        memo = [-1] * (n+1)
        memo[0] = 1
        memo[1] = 1

        return memorization(n, memo)
        

    # -------- bottom up solution --------
    def climbStairs_bottom_up(self, n: int) -> int:        
        memo = [-1] * (n+1)
        memo[0] = 1
        memo[1] = 1

        for i in range (2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]

    def climbStairs_bottom_up_optimization(self, n: int) -> int:        
        n_substract_1 = 1
        n_substract_2 = 1

        for i in range(2, n+1):
            current = n_substract_1 + n_substract_2
            n_substract_1 = n_substract_2
            n_substract_2 = current

        return n_substract_1 + n_substract_2


    # =======================================================================================================================
    # --------------------------------------------------------------------------------------------------
    # Leetcode 322. Coin Change
    # -------- bottom_up solution --------
    # Time: O(amount * len(coins))
    # Space: O(amount)
    def coinChange_bottom_up(self, coins: List[int], amount: int) -> int:
        memo = [ float('inf') ] * (amount + 1)
        memo[0] = 0     # base case: use 0 coins to make 0 cent

        # fill up the rest of the array
        for i in range (1, amount + 1):
            for coin in coins:
                if i - coin >= 0: 
                    memo[i] = min( memo[i - coin] + 1, memo[i] )

        # return the last element
        return memo[amount] if memo[amount] != float('inf') else -1

    # --------------------------------------------------------------------------------------------------
    # Leetcode 300. Longest Increasing Subsequence
    # Note: Current solution's time complexity is O(N^2) in worst case. This can be solved in O(NlogN) using Binary Search and Patience Sorting
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
        # the value in memo[i] will represent the LIS up to i-th element
        memo = [-1] * len(nums)
        memo[0] = 1     # the LIS up to slot 0 is 1 (itself)

        result = 0
        for i in range (1, len(nums)):
            max_len_LIS = 0
            # In this example, we are not sure HOW MANY SUB_PROBLEMS are there, so we have to check all of them
            for j in range (i):
                if nums[j] < nums[i]:   # only care about strictly smaller number
                    max_len_LIS = max(max_len_LIS, memo[j])
            memo[i] = max_len_LIS + 1
            result = max(result, max_len_LIS + 1)
        
        return result
    
    # O(NlogN) using Binary Search and Patience Sorting
    def lengthOfLIS_patienceSort(self, nums):
        # each of tails[i] will be the tail (smallest value) of a pile (an increasing sequence)
        tails = []

        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):           # creating a new pile
                tails.append(num)
            else:                           # append tail to an existing pile
                tails[idx] = num

        return len(tails)


    # --------------------------------------------------------------------------------------------------
    # Leetcode 139. Word Break
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
    space-separated sequence of one or more dictionary words.
    Note that the same word in the dictionary may be reused multiple times in the segmentation.
    In the following example:
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    """
    # ======== use tabulation (bottom up) ========
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)                            # search in set is O(1)
        tabulation = [False] * (len(s) + 1)
        tabulation[0] = True
        # c a t s a n d o g 
        # T F F F F F F F F

        # O(n^3): nested loop + substring computation
        for i in range (1, len(s) + 1):
            for j in range (i):
                if tabulation[j] and s[j:i] in wordDict_set:    # (1)
                    tabulation[i] = True                        # (2)
                    break; 

        return tabulation[len(s)]

        # (1): If the subproblem for s[:j] satisfied and if s[j:i] in the dict
        # (2): Substring s[0:i] CAN be segmented into a space-separated sequence of one or more dictionary words -> another subproblem satisfied


    # =======================================================================================================================
    # --------------------------------------------------------------------------------------------------
    # Leetcode 1143. Longest Common Subsequence
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Most DP problems dealing with 2 strings can be solved with a 2d array
        row = len(text1)
        col = len(text2)
        dp = [[0] * (col + 1) for _ in range (row + 1)]       # this array will be initialized with all 0s
   
        # bottom up 
        for i in range (1, row + 1):
            for j in range (1, col + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max( dp[i-1][j], dp[i][j-1] )

        return dp[row][col]


    # --------------------------------------------------------------------------------------------------
    # Leetcode 516. Longest Palindromic Subsequence
    def longestPalindromeSubseq(self, s: str) -> int:
        # Most DP problems dealing with 2 strings can be solved with a 2d array
        row, col = len(s), len(s)
        dp = [[0] * (col) for _ in range (row)]       # LPS of substring from row to col
        print(dp)
        for i in range (col):
            dp[i][i] = 1                              # LPS of a character is 1

        # bottom up
        # substringLen is the length of a possible substring that we are examining
        for substringLen in range (2, len(s)+1):
            for r in range (len(s) - substringLen+1):
                c = r + substringLen - 1
                if s[r] == s[c]:
                    dp[r][c] = dp[r+1][c-1] + 2
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r+1][c])
        
        return dp[0][len(s)-1]


    # --------------------------------------------------------------------------------------------------
    # Leetcode 5. Longest Palindromic Substring
    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        dp = [[False] * s_length for _ in range (s_length)]
        answer_len = 1                      # the length of the longest palindrom (initialized as 1 because each char is a palindrome)
        start = s_length - 1                  # where the longest palindrome starts (initialized as the last char)

        # Set up base case 1: all substrings of length 1 are palindrome (along the diagonal)
        for i in range (s_length):
            dp[i][i] = True


        # Set up base case 2: all substrings of length 2
        for i in range (s_length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                answer_len = 2
                start = i
        
        # Fill out the rest of the table (all stubstrings of length 3 and above)
        for width in range (3, s_length + 1): 
            for row in range (s_length - width + 1):
                col = row+width-1
                if s[row] == s[col] and dp[row+1][col-1]:       # if two chars are equal and the substring in middle is also a palindrome
                    dp[row][col] = True
                    answer_len = width
                    start = row

        return s[start : (start+answer_len)]
        

    # --------------------------------------------------------------------------------------------------
    # Leetcode 647. Palindromic Substrings
    """
    The idea is very similar to the above problem: Leetcode 5. Longest Palindromic Substring (even easier
    because here you only have to keep count of the number of substring)
    """
    def countSubstrings(self, s: str) -> int:
        s_length = len(s)
        dp = [[False] * s_length for _ in range (s_length)]
        count = 0
        
        # Set up base case 1: all substrings of length 1 are palindrome (along the diagonal)
        for i in range (s_length):
            dp[i][i] = True
            count += 1

        # Set up base case 2: all substrings of length 2
        for i in range (s_length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        
        # Fill out the rest of the table (all stubstrings of length 3 and above)
        for width in range (3, s_length + 1): 
            for row in range (s_length - width + 1):
                col = row+width-1
                if s[row] == s[col] and dp[row+1][col-1]:       # if two chars are equal and the substring in middle is also a palindrome
                    dp[i][i] = True
                    count += 1

        print(dp)
        return count


    # --------------------------------------------------------------------------------------------------
    # Classic 0/1 Knapsack problem
    def solveKnapsack(self, value: List[int], weights: List[int], capacity: int) -> Tuple[int, List[int]]:
        if not weights or not value: return 0
        
        # Info this memo will hold: each column represents the optimal solution at each capacity
        ogWeightsLen = len(weights)
        memo = [[0] * (capacity+1) for _ in range (ogWeightsLen + 1)]

        # Add 0-th index to value and weights so it's easier to fill the 2D array memo
        newValueList = [0] + value
        newWeightsList = [0] + weights
        print(newValueList)
        print(newWeightsList)

        # Fill up the grid
        for w in range (1, len(newWeightsList)):
            for c in range (capacity+1):
                if newWeightsList[w] > c:           # exclude
                    memo[w][c] = memo[w-1][c]
                else:                               # include
                    memo[w][c] = max( memo[w-1][c], newValueList[w]+memo[w-1][c-newWeightsList[w]] )
        
        print(memo)
        
        # Find the list of item that needed to be included
        w = len(newValueList) - 1
        c = capacity
        maxValue = memo[w][c]

        items = []
        while w != 0:
            if memo[w][c] > memo[w-1][c]:
                items.append(w-1)
                c -= newWeightsList[w]

            w -= 1

        return (maxValue, items)

    # Leetcode 474. Ones and Zeroes
    def helperCount(self, s: str) -> List[int]:
        m, n = 0, 0
        for char in s:
            if char == "0": m += 1
            else: n += 1

        return [m,n]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs: return 0
        
        ogStrsLen = len(strs)
        memo = [[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(ogStrsLen + 1)]
        print(self.get_matrix_dimensions(memo))

        print(self.print_3d_matrix(memo))
        newStrsList = [0] + strs
        # Fill up the grid
        for i_str in range (1, len(newStrsList)):
            s = newStrsList[i_str]
            m_in_s, n_in_s = self.helperCount(s)
            for n_count in range (n+1):
                for m_count in range (m+1):
                    if m_count < m_in_s or n_count < n_in_s:        # exclude
                        memo[i_str][n_count][m_count] = memo[i_str - 1][n_count][m_count]
                    else:                               # include
                        memo[i_str][n_count][m_count] = max( memo[i_str - 1][n_count][m_count], 1+memo[i_str - 1][n_count-n_in_s][m_count-m_in_s] )
        
        print(self.print_3d_matrix(memo))

        return memo[ogStrsLen][n][m]
        
    def get_matrix_dimensions(self, matrix):
        depth = len(matrix)
        rows = len(matrix[0]) if depth > 0 else 0
        cols = len(matrix[0][0]) if rows > 0 else 0
        return (depth, rows, cols)

    def print_3d_matrix(self, matrix):
        depth = len(matrix)
        for d in range(depth):
            print(f"Layer {d + 1}:")
            for row in matrix[d]:
                print("  " + " ".join(map(str, row)))  # Nicely formatted rows
            print("-" * 20)  # Separator for layers


    # --------------------------------------------------------------------------------------------------
    # Leetcode 198. House Robber ------------------------------------------
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0

        nums = [0] + nums
        memo = [0] * len(nums)
        memo[1] = nums[1]
        # print("memo: ", memo)
        # print("nums: ", nums)

        for i in range (2, len(nums)):
            memo[i] = max( nums[i]+memo[i-2], memo[i-1]  )

        # print("memo: ", memo)

        return max(memo)
    
    # Leetcode 213. House Robber II ------------------------------------------
    def classic_rob(self, og_nums: List[int], L: int, R: int) -> int:
        nums = og_nums.copy()
        nums = nums[L:R]

        print(nums)
        
        nums = [0] + nums
        memo = [0] * len(nums)
        memo[1] = nums[1]
        
        for i in range (2, len(nums)):
            memo[i] = max( nums[i]+memo[i-2], memo[i-1]  )

        return max(memo)

    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        elif len(nums) < 4: return max(nums)

        return max(self.classic_rob(nums, 0, len(nums) - 1), self.classic_rob(nums, 1, len(nums)))

    # Leetcode 337. House Robber III ------------------------------------------
    def rob3(self, root: TreeNode) -> int:
        if not root: return 0
        cache = dict()
        return self.helper_337(root, cache)

    def helper_337(self, root:TreeNode, mydict:dict) -> int:
        # base case 1
        if not root: return 0

        # base case 2
        if root in mydict:
            return mydict[root]

        # dfs
        not_rob = self.helper_337(root.left, mydict) + self.helper_337(root.right, mydict)  # not rob
        rob = root.val                                                                      # rob

        if root.left:
            rob += self.helper_337(root.left.left, mydict)
            rob += self.helper_337(root.left.right, mydict)

        if root.right:
            rob += self.helper_337(root.right.left, mydict)
            rob += self.helper_337(root.right.right, mydict)

        mydict[root] = max(rob, not_rob)

        return max(rob, not_rob)


        
        # ------------------------------------------------------------------------------
    

    # =======================================================================================================================
    # --------------------------------------------------------------------------------------------------
    # Leetcode 53. Maximum Subarray
    # Kadane’s Algorithm
    def maxSubArray(self, nums):
        # Initialize current subarray sum and overall maximum with the first element
        max_ending_sum = nums[0]
        result = nums[0]

        # Should I keep adding to the current subarray, or start fresh from here?
        for i in range(1, len(nums)):
            # 1. Starting fresh from nums[i] gives a better sum
            if max_ending_sum + nums[i] < nums[i]:
                max_ending_sum = nums[i]
            # 2. Extending the existing subarray gives a better or equal result
            else:
                max_ending_sum += nums[i]

            result = max(result, max_ending_sum)        # Update result if we've found a new maximum

        return result
    

    # ------------------------------------------------------------------------------
    # Also use a variation of Kadane's algorithms
    # Leetcode 152. Maximum Product Subarray
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currentMin, currentMax = 1, 1       # the idea is to store both the max and min products at each step

        for n in nums:
            # reset the prod calculations because multiply by 0 eliminates any prior product contribution
            if n == 0: 
                currentMin, currentMax = 1, 1
                continue
            
            # as long as n != 0, multiply n will guarantee to increase the absolute value of the product.
            # we just have to worry about the sign
            tmp = currentMax * n
            currentMax = max(currentMax * n, currentMin * n, n)
            currentMin = min(tmp, currentMin * n, n)
            res = max(res, currentMax)

        return res

    # =======================================================================================================================
    # Leetcode 10. Regular Expression Matching (Hard)  
    def isMatch(self, s: str, p: str) -> bool:
        cache = defaultdict(bool)

        return self.remDfs(s, 0, p, 0, cache)

    def remDfs(self, s: str, i: int, p: str, j: int, cache: defaultdict(bool)) -> bool:
        # Base case 0: If this node in the tree is already computed
        if (i,j) in cache: 
            return cache[(i,j)]
        # Base case 1: it is a match
        if i >= len(s) and j >= len(p):
            return True
        # Base case 2: not a match
        if j >= len(p):
            return False
        
        # Check if the first char is a match
        firstCharMatch = (i < len(s)) and (s[i] == p[j] or p[j] == '.')

        # Case 1: the next char of p is a * -> we have two choices: use or not use p[j]
        if (j+1 < len(p)) and (p[j+1] == '*'):
            # 1.1. Not Use * char
            notUse = self.remDfs(s, i, p, j+2, cache)
            cache[(i,j+2)] = notUse
            # 1.2. Use * Char. Only use if the first char is matched
            use = False
            if firstCharMatch: 
                use = self.remDfs(s, i+1, p, j, cache)
                cache[(i+1,j)] = use
            return (notUse or (firstCharMatch and use))
        
        # Case 2: the next char of p is not a *
        if (firstCharMatch):
            return self.remDfs(s, i+1, p, j+1, cache)
        
        return False


    # --------------------------------------------------------------------------------------------------
    # Leetcode 2472. Maximum Number of Non-overlapping Palindrome Substrings (Hard)
    def print_bool_matrix(self, matrix):
        if not matrix or not matrix[0]:
            print("Empty matrix")
            return

        rows, cols = len(matrix), len(matrix[0])

        # Print column indices
        header = "     " + " ".join(f"{j:2}" for j in range(cols))
        print(header)
        print("    " + "---" * cols)

        for i in range(rows):
            row_str = f"{i:2} |"  # Row index with separator
            for j in range(cols):
                cell = "T" if matrix[i][j] else "_"
                row_str += f"  {cell}"
            print(row_str)

    def maxPalindromes(self, s: str, k: int) -> int:
        # Step 1: compute the Palindrome substring 2d array
        memo = self.computePalindromeSubstringArray(s)
        # self.print_bool_matrix(memo)

        # Step 2: Call dfs to count the maximum number of substrings
        # -----------------------------------------------------------
        @lru_cache(None)
        def dfsMaxPalindrome(start) -> int:
            # Base case: no more char
            if start >= len(s): return 0

            # Option 1: skip 'start' index
            op1 = dfsMaxPalindrome(start+1)
            
            # Option 2: include all palindrome substrings starting at 'start'
            op2 = 0
            for end in range (start+k-1, len(s)):
                # if substring s[start:end] is a palindrome
                if memo[start][end]:
                    op2 = max(op2, 1 + dfsMaxPalindrome(end+1))

            return max(op1, op2)
        # -----------------------------------------------------------

        return dfsMaxPalindrome(0)
    
    

    def computePalindromeSubstringArray(self, s: str) -> List[bool]:
        memo = [[False for _ in range (len(s))] for _ in range (len(s))]

        # Case 1: each char is a palindrome
        for i in range (len(s)):
            memo[i][i] = True
        
        # Case 2: substring of len 2
        for i in range (len(s) - 1):
            if s[i] == s[i+1]:
                memo[i][i+1] = True

        # Case 3: fill out the rest of memo
        for width in range (3, len(s) + 1):
            for start in range (len(s)):
                end = start + width - 1
                if end >= len(s): continue

                if s[start] == s[end] and memo[start+1][end-1]:
                    memo[start][end] = True

        return memo

















if __name__ == "__main__":
    solution = Solution()

    # -------------------- 70 --------------------
    # print(solution.climbStairs_top_down(5))

    # -------------------- 1143 --------------------
    # a = "abcba"
    # b = "abcbcba"
    # print(solution.longestCommonSubsequence(a, b))

    # -------------------- 674 --------------------
    # a = "aaaaa"
    # print(solution.countSubstrings(a))

    # -------------------- 474 --------------------
    # value = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # weight = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # capacity = 15
    # print(solution.solveKnapsack(value, weight, capacity))

    # strs = ["10","0001","111001","1","0"]
    # m = 5
    # n = 3
    # print(solution.findMaxForm(strs, m, n))

    # -------------------- 300 --------------------
    # print( solution.lengthOfLIS_patienceSort([10,9,2,5,3,7,101,18]) )

    # -------------------- 516 --------------------
    # print( solution.longestPalindromeSubseq("cbbd") )

    # -------------------- 10 --------------------
    # s = "aaaaaaaaaaaaaaaaaaa"
    # p = "a*a*a*a*a*a*a*a*a*b"
    # print( solution.isMatch(s, p) )

    # -------------------- 2472 --------------------
    s = "iqqibcecvrbxxj"
    print(solution.maxPalindromes(s, 1))


