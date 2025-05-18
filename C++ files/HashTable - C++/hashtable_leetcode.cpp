/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Hash Table =========================================================
1) Design a Hash Table without using any built-in hash table libratries
    a) Leetcode 705. Design HashSet
    b) Leetcode 706: Design HashMap
2) Leetcode 128. Longest Consecutive Sequence

*/ 

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // Leetcode 128. Longest Consecutive Sequence
    int longestConsecutive(vector<int>& nums) {
        unordered_set <int> set;
        // insert all elements in nums into a set: O(n) 
        for (int x : nums){
            set.insert(x); 
        }
        
        int count = 0; 
        int max = 0; 
        
        // loop through each nums: O(n)
        for (int x : nums){
            // check if x is the start of a sequence: O(1)
            if (set.find(x-1) == set.end()){ 
                count = 1; 
                int current = x + 1; 
                while (set.find(current) != set.end()) { // current is in the set
                    count++; 
                    current++; 
                }
                max = std::max(count, max);
            }
        }
        
        return max;
    }



};















