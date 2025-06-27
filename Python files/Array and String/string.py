"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Array =========================================================

1. Leetcode 72. Edit Distance


"""

from typing import List
from collections import Counter
import copy

class Solution:
    # ------------------------------------------------------------------------------
    # (Also a DP problem)
    # Leetcode 72. Edit Distance
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        # create a dp table to store sub-problems
        dp = [[0 for _ in range (len1+1)] for _ in range (len2+1)]

        # base case will be first row and column of the table
        # populate the base case
        for i in range (len1 + 1): 
            dp[0][i] = i
        
        for k in range (len2 + 1):
            dp[k][0] = k

        # populate the rest of the table
        for r in range (1, len2 + 1):
            for c in range (1, len1 + 1):
                subproblem = min( dp[r-1][c-1], dp[r-1][c], dp[r][c-1] )
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = subproblem + 1

        return dp[len2][len1]



























if __name__ == "__main__":
    leetcode = Solution()

    # --------------------------- 15 ---------------------------





