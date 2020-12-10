class Solution:
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
                

if __name__ == "__main__":
    # ------------------------------------------------------------
    sol = Solution()
    # reverse_vowels = sol.reverseVowels('leetcode')  
    # print(reverse_vowels)

    # ------------------------------------------------------------
    print(sol.nthUglyNumber(10))
    

