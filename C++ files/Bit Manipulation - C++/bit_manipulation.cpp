/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Bit Manipulation =========================================================
1) Check if a given number is a power of 2 
    Leetcode 231. Power of Two
2)  Count the number of ones in the binary representation of the given number
    Leetcode 191. Number of 1 Bits
    Leetcode 338. Counting Bits
    O(K) where K is the number of 1s 
3) Hamming Distance
    Leetcode 461. Hamming Distance
    Leetcode 477. Total Hamming Distance
4) All posible subsets
    Leetcode 78. Subsets

*/ 

#include <vector>
#include <iostream>
#include <math.h>

class Solution {
public:
    // Leetcode 231. Power of Two
    bool isPowerOfTwo(int n) {
        if (n < 0) 
            return false; 
        
        return (n && !(n & (n - 1)));
    }


    // Count the number of ones in the binary representation of the given number.
    // Leetcode 191. Number of 1 Bits
    int count_one (int n)
    {
        int count = 0; 
        while( n ) {
            n = n & (n-1);
            count++;
        }
        return count;
    }


    // Hamming Distance
    // Leetcode 461. Hamming Distance
    // Idea: XOR the two integer (XOR will yields 1 only when both bits are different). Then count 1s in XOR 
    int hammingDistance(int x, int y) {
        int XxorY = x^y;
  
        return count_one(XxorY);        
    }

    // Leetcode 477. Total Hamming Distance
    // Idea: Loop through each bit, count # of 1s and 0s for that bit for every number
    // the total HD for THAT BIT will be (# 1s * # 0s)
    int totalHammingDistance(std::vector<int>& nums) {
        int total = 0; 
        for (int i = 0; i<32; i++){
            int one_s = 0;
            int zero_s = 0;
            for (int k = 0; k < nums.size(); k++){  
                if ((nums[k] & 1) == 1) { // if this digit is 1
                    one_s++;
                } else {
                    zero_s++; 
                }
                nums[k] = nums[k] >> 1;
            } 
            total += (one_s * zero_s); 
        }
        
        return total;
    }


    // Leetcode 78. Subsets
    /* 
    Idea: Use Bit Maniupation. There are 2^N subsets. Use nested for loop
    Loop i from 0 to 2^size and use i's binary representation to 
    represent one of the subset
        Then the inside for loop will loop j from 0 to size
        Use (i & (1<<j)) to decide if we will put that element jth in ith subset
    */
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        int size = nums.size();
        // data structure
        std::vector<std::vector<int>> result; 
        
        // represent all possible subsets   
        for(int i = 0; i < pow(2, size); i++) { 
            std::vector<int> subset; 
            // represent each element
            for(int j = 0; j < size; j++) { 
                // check if the jth element is chosen for the ith subset
                if ( i & (1<<j) ) { 
                    subset.push_back(nums[j]); 
                }
            }
            result.push_back(subset); 
        }
        
        return result; 
    
    }; // O(2^N * N)

};















