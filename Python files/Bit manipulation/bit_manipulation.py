"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Bit Manipulation =========================================================
Construct binary representation of an int
    Solution 1: Manual conversion
    Solution 2: Bitwise operations (& and >>)
Construct an int from binary representation
    Leetcode 1290. Convert Binary Number in a Linked List to Integer
Check if a given number is a power of 2 
    Leetcode 231. Power of Two
    Right below, we learnt that n&(n-1) will reduce one 1 in the binary repre of n
    A number that is a power of 2 will only have one 1 in its binary repre
    --> Property of a number that is a power of 2: n&(n-1) will be 0
Count the number of ones in the binary representation of the given number
    Leetcode 191. Number of 1 Bits
    Leetcode 338. Counting Bits
    O(K) where K is the number of 1s 
Check if i-th bit is a set (1) or not (0)
    Same idea for checking if a number if odd -> (x&1) because its binary repre will have 1 as LSB
    Same idea for i-th bit: shift the 1 to the apprepriate place then do the &
Hamming Distance
    Leetcode 461. Hamming Distance
    Leetcode 477. Total Hamming Distance
All posible subsets
    Leetcode 78. Subsets

    
More leetcodes    
    Leetcode 1545. Find Kth Bit in Nth Binary String
"""

from typing import List
from collections import Counter
from collections import defaultdict
import copy
import math


""" Check out the bit_manipulation.cpp file in C++ folder """
class Solution:
    # Solution 1: Manual conversion
    def int2BinarySolution1(self, n: int) -> str:
        if n == 0: return "0"

        bits = []
        while n > 0:
            bits.append( str( int(n % 2) ) )
            n = int(n/2)

        return ''.join(reversed(bits))    

    # Solution 2: Bitwise operations (& and >>)
    def int2BinarySolution2(self, n: int) -> str:
        if n == 0: return "0"

        bits = []
        while n > 0:
            bits.append( str( n & 1 ) )
            n = (n >> 1)

        return ''.join(reversed(bits))    

    # Leetcode 1290. Convert Binary Number in a Linked List to Integer
    def getDecimalValue(self, binary_representation: List[int]) -> int:
        result = 0
        # (result << 1) will shift all bits one spot to the left
        # if bit is 0 -> 00000000
        # if bit is 1 -> 00000001
        # doing this OR operation will add one more bit to the end of our result, whether it's 0 or 1
        for bit in binary_representation: 
            result = (result << 1) | bit
            head = head.next

        return result
    
    # ----------------------------------------------------------------------------------
    # Same idea for checking if a number if odd -> (x&1) because its binary repre will have 1 as LSB
    # Same idea for i-th bit: shift the 1 to the apprepriate place then do the &
    def is_ith_bit_set(self, n: int, i: int) -> bool:
        return ( n & (1<<i) )


    # ----------------------------------------------------------------------------------
    # Leetcode 1545. Find Kth Bit in Nth Binary String
    def complementBinary(self, s: str) -> str:
        result = ""
        for bit in s:
            if bit == "0":
                result += "1"
            else:
                result += "0"
        
        return result

    def findKthBitBruteForce(self, n: int, k: int) -> str:
        s = "0"         # s1
        
        for _ in range (1, n):
            invertedS = self.complementBinary(s)
            s = s + "1" + invertedS[::-1]
            print(s)

        return s[k-1]

    """
    ✨ Clever Insight
    Each Sₙ is a palindrome with a '1' in the middle. So:
    - If k is the middle index → return '1'
    - If k is in the first half → recurse into Sₙ₋₁
    - If k is in the second half → map it to the mirrored index in the first half, recurse, then invert the result
    """
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: 
        if n == 1:
            return '0'
        
        # Length of Sₙ is 2ⁿ - 1
        length = (1 << n) - 1  
        mid = length // 2 + 1

        # Case 1: Found k-th
        if k == mid:
            return '1'
        # Case 2: k is in the first half
        elif k < mid:
            return self.findKthBit(n - 1, k)
        # Case 3: k is in the second half
        else:
            mirrored_k = length - k + 1
            bit = self.findKthBit(n - 1, mirrored_k)
            return '1' if bit == '0' else '0'


    # ----------------------------------------------------------------------------------
    """
    - For each bit position (0 to 30), count how many numbers have a 1 and how many have a 0.
    - Each differing pair at that bit contributes 1 to the total Hamming distance.
    - So, for bit i, the contribution is: count_ones * count_zeros
    """
    # Leetcode 477. Total Hamming Distance
    # 31 bit positions × n elements -> O(n)
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        # 0 to 30 covers all bits for 32-bit integers
        for i in range(31):  
            # Count number of 1s for bit i-th
            count_ones = 0
            for num in nums:
                count_ones += (num >> i) & 1 
            # If the bit is not 1, it's 0
            count_zeros = n - count_ones
            # Contribution to HD in bit i-th
            total += count_ones * count_zeros

        return total

   
            
    























if __name__ == "__main__":
    leetcode = Solution()

    # ------------------------------------------
    # print(leetcode.int2BinarySolution1(100))
    # print(leetcode.int2BinarySolution2(100))

    # ------------------ 1545 ------------------
    # print(leetcode.findKthBit(4, 11))