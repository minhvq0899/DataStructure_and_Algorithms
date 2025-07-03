"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Array =========================================================

Easy
1. Leetcode 345: Reverse Vowels of a String
2. Leetcode 344: Reverse String
----------------------------------------------------
3. Leetcode 72. Edit Distance

----------------------------------------------------
Hard
4. Leetcode 273. Integer to English Words 




"""

from typing import List
from collections import Counter, defaultdict
import copy

class Solution:
    # Leetcode 345: Reverse Vowels of a String
    def reverseVowels(self, s: str) -> str:
        vowels = 'aieouAIEOU'
        s = list(s)
        i = 0
        j = len(s) - i - 1
        while i < len(s) and j > -1:
            # we have to consider this case first
            if i >= j:
                break
            # switch
            if (s[i] in vowels) and (s[j] in vowels):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in vowels and s[j] not in vowels:
                i += 1
                j -= 1
            elif s[i] in vowels and s[j] not in vowels:
                j -= 1
            elif s[i] not in vowels and s[j] in vowels:
                i += 1

        return ''.join(s)

    # -------------------------------------------------------------------------------
    # Leetcode 344: Reverse String
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range (0, len(s), 2*k):
            # assign j
            if (len(s) < k) or (i + k - 1 >= len(s)): # If there are less than k characters left
                j = len(s) - 1
            else:
                j = i + k - 1
            # check if j is out of bound
            if j >= len(s): break
            # reverse part
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
        return ''.join(s)

    # ==============================================================================
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

    # ==============================================================================
    # Leetcode 273. Integer to English Words (Hard)
    unit = {0: "", 1: "Thousand", 2: "Million", 3: "Billion"}
    first_level_to_str = {0: "", 1: "One ", 2: "Two ", 3: "Three ", 4: "Four ", 5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine "}
    second_and_third_level_to_str = {2: "Twent", 3: "Thirt", 4: "Fourt", 5: "Fift", 6: "Sixt", 7: "Sevent", 8: "Eight", 9: "Ninet"}
    def helper_273(self, num: int, level: int) -> str:    
        each_digit = []
        while num > 0:
            remainder = num % 10
            each_digit.append(remainder)
            num = int(num/10)

        sub_result = ""
        for i in range (len(each_digit) - 1, -1, -1):
            d = each_digit[i]
            if i == 2: sub_result += self.first_level_to_str[d] + "Hundred" + " "
            elif i == 1:
                if d == 0: 
                    continue
                elif d == 1: 
                    zeroth_d = each_digit[0]        # if i == 1, there will DEFINITELY be a 0th digit
                    if zeroth_d == 0:
                        sub_result += "Ten" + " " + self.unit[level] + " "
                    elif zeroth_d == 1: 
                        sub_result += "Eleven" + " " + self.unit[level] + " "
                    elif zeroth_d == 2: 
                        sub_result += "Twelve" + " " + self.unit[level] + " "
                    else:
                        sub_result += self.second_and_third_level_to_str[zeroth_d] + "een" + " " + self.unit[level] + " "
                    return sub_result 
                elif d == 4: 
                    sub_result += "Forty" + " "
                else: 
                    sub_result += self.second_and_third_level_to_str[d] + "y" + " "
                    
            elif i == 0: sub_result += self.first_level_to_str[d]
        
        if not sub_result: return ""
        
        sub_result += self.unit[level] + " "

        return sub_result

    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"

        three_digit = []
        while num > 0:
            remainder = num % 1000
            three_digit.append(remainder)
            num = int(num/1000)

        result = ""
        for i in range (len(three_digit)):
            result = self.helper_273(three_digit[i], i) + result 

        return result.rstrip()















if __name__ == "__main__":
    leetcode = Solution()






