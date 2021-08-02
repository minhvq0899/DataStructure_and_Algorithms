/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= DFS BFS with template =========================================================
1) Leetcode 216. Combination Sum III
2) Leetcode 40. Combination Sum II
3) Leetcode 377. Combination Sum IV

*/ 

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // Leetcode 216. Combination Sum III
    void combination_count(int k, vector<int> &potential, int target, vector<vector<int>> &result, int start) {
        // base case 1
        if ((target == 0) && (k == 0)) {
            result.push_back(potential); 
            return; 
        } 
        // base case 2
        if ((target < 0) || (k == 0)) {
            return; 
        }

        for (int i = start; i < 10; i++) {
            potential.push_back(i); 
            // dfs
            combination_count(k-1, potential, target-i, result, i+1); 
            // backtracking
            potential.pop_back(); 
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result; 
        vector<int> potential; 

        combination_count(k, potential, n, result, 1); 
        return result;
    }





    // ================================================================================================================================================================================================================
    // Leetcode 40. Combination Sum II
    vector<vector<int>> result2; 
    vector<int> potential2; 

    void combination_count2(vector<int>& candidates, int target, int start) {
        // base case 1
        if (target == 0) {
            this->result2.push_back(this->potential2); 
            return; 
        } 
        // base case 2
        if (target < 0) {
            return; 
        }

        for (int i = start; i < candidates.size(); i++) {
            if ( (i>start) && (candidates[i] == candidates[i-1]) ) continue; // avoid duplicate

            this->potential2.push_back(candidates[i]); 
            // dfs
            combination_count2(candidates, target-candidates[i], i+1); 
            // backtracking
            this->potential2.pop_back(); 
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end()); 

        combination_count2(candidates, target, 0); 
        
        return this->result2;
    }


    // =====================================================================================================================================================================================================================
    /*
    int result4 = 0; 
    vector<vector<int>> ans;
    
    // Leetcode 377. Combination Sum IV
    void combination_count4(vector<int>& nums, vector<int> &potential, int target, int start) {
        // base case 1
        if (target == 0) {
            this->result4++;
            this->ans.push_back(potential); 
            return; 
        } 
        // base case 2
        if (target < 0) {
            return; 
        }

        for (int i = start; i < nums.size(); i++) {
            potential.push_back(nums[i]); 
            // dfs
            combination_count4(nums, potential, target-nums[i], i); 
            // backtracking
            potential.pop_back(); 
        }
    }

    vector<vector<int>> combinationSum4(vector<int>& nums, int target) { 
        vector<int> potential; 

        combination_count4(nums, potential, target, 0); 
        return this->ans;
    }
    */


    // ================================================================================================================================================================================================================
    vector<vector<int>> result797; 
    vector<int> path; 
    // Leetcode 797. All Paths From Source to Target
    void dfs797(vector<vector<int>>& graph, int start) {
        // base case 
        if (start == graph.size() - 1) {
            this->result797.push_back(path); 
            return;
        }

        for (int neighbor : graph[start]) {
            this->path.push_back(neighbor);
            dfs797(graph, neighbor); 
            this->path.pop_back(); 
        }
    }

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        this->path.push_back(0); 
        dfs797(graph, 0); 
        return this->result797; 
    }

};


int main() {
    Solution solution; 
    vector<int> candidates {2,5,2,1,2}; 
    int target = 5;
    vector<vector<int>> result = solution.combinationSum2(candidates, target); 
    for (vector<int> it : result) {
        for (int x : it) {
            cout << x << " "; 
        }
        cout << "\n"; 
    }

    
    // ----------------------------------------------------------------------------
    // vector<int> nums {1,2,3}; 
    // int target = 4;
    // vector<vector<int>> ans = solution.combinationSum4(nums, target); 

    // for (vector<int> it : ans) {
    //     for (int x : it) {
    //         cout << x << " "; 
    //     }
    //     cout << "\n"; 
    // }


    // ----------------------------------------------------------------------------

    return 0;
}














