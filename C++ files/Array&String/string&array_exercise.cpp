/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= String and Array =========================================================
1) Implement an algorithm to determine if a string has all unique characters. What if you cannot use 
additional data structures? (Assuming the string is of ASCII type)

2)  Leetcode 567: Permutation in String: Given two strings s1 and s2, return true if s2 CONTAINS the permutation of s1.
    1.2. Given two strings, write a method to decide if one IS a permutation of the other. 

3)  1.4 or leetcode 226: Palindrome Permutation
    Given a string, determine if a permutation of the string could form a palindrome.

4)

5) Leetcode 325: Maximum Size Subarray Sum K
6) Leetcode 5. Longest Palindromic Substring
7) Leetcode 15. 3Sum
*/ 

#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm> 
#include <limits>
#include <math.h>
using namespace std;
//#include <bits/stdc++.h>


class string_exercises {
public:
    string_exercises(){}; 

    /**
    1.1. Implement an algorithm to determine if a string has all unique characters. What if you
    cannot use additional data structures? (Assuming the string is of ASCII type)
        1. The first idea is to create an array of boolean values
            Time: O(n)
            Space: O(1) 

        2. If we are not allowed to use additional data structures, we can:
            a) Compare each char to every other char -> time complexity is O(n^2)
            b) If we can modify the input string, we can sort the string -> O(n*logn)
    */
    bool isUniqueChars(std::string str) {
        // if the length of the string is more than the length of the ascii table (128),
        // return false
        if (str.size() > 128) return false; 

        // create a bool array of size 128
        bool bool_array[128] = {false};

        // loop through each char of str
        for (char& c : str) {
            if ( !bool_array[int(c)] ) {
                bool_array[int(c)] = true; 
            } else {
                return false; 
            }
        }

        return true; 
    }

    // ---------------------------------------------------------------------------------------------

    /**
    Leetcode 567: Permutation in String: Given two strings s1 and s2, return true if s2 CONTAINS the permutation of s1.
    1.2. Given two strings, write a method to decide if one IS a permutation of the other. 
    */
    bool checkInclusion_array(std::string s1, std::string s2) {
        // if s1 is longer than s2 -> false
        if (s1.length() > s2.length()) return false; 

        // create an array storing the frequency of each char in s1
        int s1map[26] = {0}; 
        for (char& c : s1) {
            s1map[ int(c)-97 ]++; 
        }

        char c; 
        // iterate through s2
        for (int i = 0; i <= s2.length() - s1.length(); i++) {
            int s2map[26] = {0}; 
            // add each char in a permutation from s2
            for (int k = 0; k < s1.length(); k++){
                c = s2.at(k + i); 
                s2map[ int(c)-97 ]++; 
            }
            // compare 
            if (checkPermutation(s1map, s2map)) {
                return true; 
            }   
        }
        return false; 
    }

    bool checkPermutation(int s1[], int s2[]){
        for (int i = 0; i < 26; i++) {
            if (s1[i] != s2[i]) {
                return false; 
            }
        }
        return true; 
    }

    // Another way to optimize it
    // bool checkInclusion_slidingwindow(std::string s1, std::string s2) {}

    // ---------------------------------------------------------------------------------------------------

    /**
    1.4 or leetcode 226: Palindrome Permutation
    Given a string, determine if a permutation of the string could form a palindrome.
    */
    // ----------------- first implementation: count the frequency of each char -----------------
    bool isPermutationOfPalindrome(std::string phrase) {
        // create a set
        std::unordered_set<char> myset; 

        for (char& c : phrase) {
            if (myset.count(c)){          // if we find the char c in our set
                myset.erase(c); 
            } else {                      // if we cannot find the char c in our set
                myset.insert(c); 
            }
        }
        return (myset.size() <= 1); 
    }

    // ----------------- Another clever implementation -----------------
    bool isPermutationOfPalindrome_bit_manipulation(std::string phrase) {
        int bitVector = createBitVector(phrase); 

        // now just have to check if the bitVector have at most 1
        // meaning either it is 0 or it is a power of two
        return (bitVector == 0) || exactlyOneBit(bitVector); 
    }

    // helper 1: create a bit vector (size = 26) for the string
    int createBitVector(std::string phrase) {
        int bitVector = 0; 

        int ascii; 
        for (char& c : phrase) {
            ascii = int(c) - 97;  
            bitVector = toggle(bitVector, ascii); 
        }

        return bitVector; 
    }

    // helper 2: toggle the i-th bit
    int toggle(int bitVector, int index) {
        if (index < 0) return bitVector; 

        int mask = 1 << index; 
        if ( (bitVector & mask) == 0 ) {
            bitVector = (bitVector | mask);         // off -> on
        } else {
            bitVector = (bitVector & ~mask);        // on -> off 
        }

        return bitVector; 
    }

    // helper 3: check if exactly one bit is 1 (equilavent to checking if a number if a power of 2)
    bool exactlyOneBit(int bitVector) {
        int subtractOne = bitVector - 1; 
        return ((bitVector & subtractOne) == 0); 
    }


    // --------------------------------------------------------------------------------------------------
    /**
    There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.
        EXAMPLE
        pale, ple -> true
        pales, pale -> true
        pale, bale -> true
        pale, bae -> false
    */
    bool oneEditAway(std::string first, std::string second) {
        bool result = false; 

        // insert
        if (first.length() + 1 == second.length()) {
            result = oneInsertAway(first, second); 
        } else if (first.length() - 1 == second.length()) {
            result = oneDeleteAway(first, second); 
        } else if (first.length() == second.length()) {
            result = oneReplaceAway(first, second); 
        }

        return result; 
    }

    bool oneDeleteAway(std::string first, std::string second) {
        // string second will be shorter than first
        int strike = 1; 
        int ifirst = 0;
        int isecond = 0; 

        // two pointer
        while (isecond < second.length()){
            if ( first[ifirst] != second[isecond] ) {
                if (strike > 0) {
                    strike--; 
                    ifirst++; 
                    continue; 
                } 
                else return false; 
            }
            ifirst++;
            isecond++;
        }

        return true; 
    }

    
    bool oneInsertAway(std::string first, std::string second) {
        // string second will be LONGER than first
        int strike = 1; 
        int ifirst = 0;
        int isecond = 0; 

        // two pointer
        while (ifirst < first.length()){
            if ( first[ifirst] != second[isecond] ) {
                if (strike > 0) {
                    strike--; 
                    isecond++; 
                    continue; 
                } 
                else return false; 
            }
            ifirst++;
            isecond++;
        }

        return true; 
    }
    
    bool oneReplaceAway(std::string first, std::string second) {
        // two strings will have equal lengths
        int strike = 1; 
        int ifirst = 0;
        int isecond = 0; 

        // two pointer
        while (isecond < second.length()){
            if ( first[ifirst] != second[isecond] ) {
                if (strike > 0) strike--; 
                else return false; 
            }
            ifirst++;
            isecond++;
        }

        return true; 
    }


    // =================================================================================================
    // Leetcode 325: Maximum Size Subarray Sum K
    int maxSubArrayLen(vector<int>& nums, int k) {
        // Brute force: have two for loops -> O(n^2)
        // If we ust Hash Map, we can bring the complaxity down to O(n)
        // Idea: The Hash Map will have: key is sum from 0th index to ith index, value is the ith index
        unordered_map<int, int> map; 
        int max_len = 0; 
        
        for (int i = 0, sum = 0; i < nums.size(); i++) {
            sum += nums[i]; 
            if (map.find(sum) == map.end()) {   // sum hasn't occurred before
                map[sum] = i;                   // this mean sum of subarray from 0 to ith index is 'sum'
            } 
            // if the sum of (current 'sum' - k) is in the map/ has occured before at index jth, that means 
            // the sum of subarray from jth to ith must be k -> found a match
            if (map.find(sum-k) != map.end()) {   
                max_len = max(max_len, i - map[sum-k]); 
            }
            // if sum == k, that means the sum of subarray from 0 to ith is k -> found another match
            if (sum == k) {
                max_len = max(max_len, i+1); 
            }
        }

        return max_len; 
    }


    // =================================================================================================
    // Leetcode 5. Longest Palindromic Substring
    string longestPalindrome(string s) {
        int len = s.length(); 
        vector<vector<bool>> dp (len, vector<bool> (len, false)); 
        int start = len-1; 
        int max_len = 1; 

        for (int i = 0; i < len - 1; i++) {
            dp[i][i] = true;
            if (s[i] == s[i+1]) {
                dp[i][i+1] = true; 
                max_len = 2; 
                start = i; 
            } 
        }
        dp[len-1][len-1] = true; 

        for (int width = 3; width < len + 1; width++) {
            for (int row = 0; row < len - width + 1; row++) {
                int col = row + width - 1; 
                if ( (s[row] == s[col]) && dp[row+1][col-1] ) {
                    dp[row][col] = true; 
                    max_len = width; 
                    start = row; 
                }
            }
        }

        return s.substr(start, max_len); 
    }






    // =================================================================================================
    // Leetcode 15. 3Sum
    // vector<vector<int>> threeSum(vector<int>& nums) {
        
    // }





















    // =================================================================================================





}; 



  



int main() {
    return 0; 
}





