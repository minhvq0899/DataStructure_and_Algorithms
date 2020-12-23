"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================== Two Pointers Exercise ==============================================
1234. Replace the Substring for Balanced String

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.
"""

class Solution:
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


if __name__ == "__main__":
    balanceStr = Solution()
    print('Answer is: ', balanceStr.balancedString('EQRWQQQW'))
            