"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Array =========================================================

Easy
Leetcode 345: Reverse Vowels of a String
Leetcode 344: Reverse String

----------------------------------------------------
(KMP algorithm)
Leetcode 1408. String Matching in an Array (using KMP algorithm makes it a Medium)
Leetcode 214. Shortest Palindrome
Leetcode 1392. Longest Happy Prefix


Leetcode 72. Edit Distance
Leetcode 1347. Minimum Number of Steps to Make Two Strings Anagram (simply use Counter - don't overthink)

----------------------------------------------------
Hard
Leetcode 273. Integer to English Words 
Leetcode 68. Text Justification




"""

from typing import List
from collections import Counter, defaultdict
import copy
import math

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
                    dp[r][c] = subproblem + 1       # it takes one additional operation

        return dp[len2][len1]


    # -------------------------------------------------------------------------------
    # Leetcode 1408. String Matching in an Array (using KMP algorithm makes it a Medium)
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and self.kmp_search(word2, word1):
                    res.append(word1)
                    break
        return res

    def build_lps(self, pattern: str) -> List[int]:
        # Longest Prefix Suffix array
        lps = [0] * len(pattern)
        length = 0                      # length of the previous longest prefix suffix

        for i in range(1, len(pattern)):
            # Up to index ith, the longest prefix suffix seen in pattern[:i] was length
            # Meaning the first length number of chars are the same as the last length number of chars
            # So when we see an unmatching char between pattern[i] and pattern[length], we need to look at the longest prefix suffix of (length-1) 
            # Example: if length is currently 3, meaning the first 3 chars of pattern match with the last 3 chars leading up to i-th (excluding pattern[i]) 
            # So if pattern[i] != pattern[length], we go back one step to see if the first 2 chars of pattern match with the last 2 chars (including pattern[i])
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]
            # If it matches, simply keep increasing
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
        return lps

    def kmp_search(self,text: str, pattern: str) -> bool:
        lps = self.build_lps(pattern)
        i = j = 0  # i for text, j for pattern

        # This while loop logic is similar to the logic in building lps
        # We also iterate i from 0 to len(text)
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == len(pattern):
                    return True  # match found
            # If unmatch, we go back one step to see if the first (j-1) chars of pattern match with the last (j-1) chars (including text[i])
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False
    

    # -------------------------------------------------------------------------------
    # Leetcode 214. Shortest Palindrome
    # Idea: we want to find the longest palindromic prefix of the string. Once we know that, we can reverse the remaining suffix and prepend it
    def shortestPalindrome(self, s: str) -> str:
        # ------------------------------------------------
        def build_lps(pattern: str) -> List[int]:
            lps = [0] * len(pattern)
            length = 0      # length of longest previous prefix suffix

            for i in range (1, len(lps)):
                while length > 0 and pattern[i] != pattern[length]:
                    length = lps[length - 1]
                
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length

            return lps
        # ------------------------------------------------
        reversed_s = s[::-1]                    # reversed s
        combined = s + "#" + reversed_s         # combined s + reversed_s to find the longest palindromic prefix (lpp)

        lps = build_lps(combined)               # after building lps on the combined str, the lpp wil be the value at lps[-1] 
        # print(combined)
        # print(lps)
        lpp = lps[-1]
        toAdd = s[lpp:][::-1]

        return toAdd + s

    # -------------------------------------------------------------------------------
    # Leetcode 1392. Longest Happy Prefix
    def longestPrefix(self, s: str) -> str:
        # -------------------------------------------------
        def build_lps(pattern: str) -> List[int]:
            lps = [0] * len(pattern)
            length = 0      # length of previous longest prefix suffix

            for i in range (1, len(lps)):
                while length > 0 and pattern[i] != pattern[length]:
                    length = lps[length - 1]
                
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
            
            return lps
        # -------------------------------------------------
        lps = build_lps(s)
        print(lps)
        lengthOfLps = lps[-1]

        return s[:lengthOfLps]
    



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

    
    # -------------------------------------------------------------------------------
    # Leetcode 68. Text Justification
    # Ex: eachResultWord = ["This", "is", "an"], whiteSpaceLen = 8  ---> return "This    is    an"
    def prepareNewLine(self, line_words, whiteSpace_len) -> str: 
        gaps = len(line_words) - 1
        space, extra = divmod(whiteSpace_len, gaps)
        result = ""

        # Case 1: If whiteSpace_len can be divided evenly between each word
        if extra == 0: 
            for i in range(gaps):
                result += line_words[i]
                result += (" " * space)
            result += line_words[-1]        # Add last word without extra space
        # Case 2: 
        else:
            for i in range(gaps):
                result += line_words[i]
                # This means for each extra space we have, we evenly divide them into each left-most space
                real_space = space + (1 if i < extra else 0)
                result += (" " * real_space)
            result += line_words[-1]        # Add last word without extra space

        return result   

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        result = []

        while i < len(words):
            # reset
            line_words = []
            line_len = 0

            # Greedily pack words into the current line
            while i < len(words):
                word_len = len(words[i])
                # len(line_words) == number of white space
                if line_len + len(line_words) + word_len > maxWidth:
                    break
                line_words.append(words[i])
                line_len += word_len
                i += 1

            # Determine if this is the last line
            is_last_line = (i == len(words))

            # Case 1: Last word or line_words has len 1
            if is_last_line or len(line_words) == 1:
                # Left-justified: words separated by single space, pad end 
                line = " ".join(line_words)
                line += (" " * (maxWidth-len(line)))
            # Case 2: Fully justified - distribute spaces evenly
            else:
                # Compute how many white space between each word
                whiteSpace_len = maxWidth - line_len
                line = self.prepareNewLine(line_words, whiteSpace_len)

            result.append(line)
                
        print(result)
        return result
                


























if __name__ == "__main__":
    leetcode = Solution()

    # ------------------ LC 72: Edit Distance ------------------
    # word1 = "horse"
    # word2 = "ros"
    # leetcode.minDistance(word1, word2)

    # ------------------ LC 1408. String Matching in an Array ------------------
    # pattern = "ACACAAAC"
    # print(leetcode.build_lps(pattern))

    # ------------------ LC 214 ------------------
    # s = "abcd"
    # print(leetcode.shortestPalindrome(s))

    # ------------------ LC 1392 ------------------
    # s = "ababab"
    # print(leetcode.longestPrefix(s))

    # ------------------ LC 68 ------------------
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    leetcode.fullJustify(words, maxWidth)
    # print( leetcode.prepareNewWord( ["Science","is","what","we"], 20) )