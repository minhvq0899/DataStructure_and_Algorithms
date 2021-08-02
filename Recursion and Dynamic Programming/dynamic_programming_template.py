"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================= Template for Dynamic Programming =========================================
1. Leetcode 70: Climbing Stairs
2. Leetcode 322. Coin Change
3. Leetcode 300. Longest Increasing Subsequence
4. Leetcode 139. Word Break
5. Leetcode 1143. Longest Common Subsequence
6. Leetcode 516. Longest Palindromic Subsequence
7. Leetcode 5. Longest Palindromic Substring
8. Leetcode 647. Palindromic Substrings
9. Classic 0/1 Knapsack Problem
10. Leetcode 337. House Robber III

"""

from typing import List
from array import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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



    # ==================================================================================================
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


    # ==================================================================================================
    # Leetcode 300. Longest Increasing Subsequence
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
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



    # ==================================================================================================
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


    # ==================================================================================================
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



    # ==================================================================================================
    # Leetcode 516. Longest Palindromic Subsequence
    def longestPalindromeSubseq(self, s: str) -> int:
        # Most DP problems dealing with 2 strings can be solved with a 2d array
        row, col = len(s), len(s)
        dp = [[0] * (col) for _ in range (row)]       # LPS of substring from row to col
        for i in range (col):
            dp[i][i] = 1                              # LPS of a character is 1

        # bottom up
        for width in range (2, len(s)+1):
            for r in range (len(s)-width+1):
                c = r + width - 1
                if s[r] == s[c]:
                    dp[r][c] = dp[r+1][c-1] + 2
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r+1][c])
        
        return dp[0][len(s)-1]


    # ==================================================================================================
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
        

    # ==================================================================================================
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


    # ==================================================================================================
    # Classic 0/1 Knapsack problem
    def solveKnapsack(self, value: List[int], weights: List[int], capacity: int) -> int:
        # basic check
        if capacity <= 0 or not value or len(value) != len(weights):
            return 0
        
        v_len = len(value)
        w_len = len(weights)

        # each position in this matrix will hold the max value that we can form with a capacity 
        dp = [[0] * (capacity+1) for _ in range (v_len) ]       # or w_len same idea

        # base case row 0th: which cap can hold the first item
        for c in range (1, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = value[0]
        
        # now just fill out the rest of the table
        for row_or_w in range (1, w_len): 
            for col_or_c in range (1, capacity + 1):
                sum1 = dp[row_or_w - 1][col_or_c]                       # exclude
                
                sum2 = value[row_or_w]                                  # include
                if col_or_c - weights[row_or_w] > 0:
                    sum2 += dp[row_or_w - 1][col_or_c - weights[row_or_w]]
                
                dp[row_or_w][col_or_c] = max(sum1, sum2)
        
        print(dp)
        return dp[w_len-1][capacity]


    # ==================================================================================================
    # Leetcode 337. House Robber III
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        mydict = dict()
        return self.helper_337(root, mydict)

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
























if __name__ == "__main__":
    solution = Solution()
    # print(solution.climbStairs_top_down(5))

    # a = "abcba"
    # b = "abcbcba"
    # print(solution.longestCommonSubsequence(a, b))

    # a = "aaaaa"
    # print(solution.countSubstrings(a))

    value = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50
    print(solution.solveKnapsack(value, weight, capacity))






