/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Union Find =========================================================
1) Leetcode 684. Redundant Connection 

*/ 

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Union_by_rank {
public:
    vector<int> parents; 
    vector<int> rank;

    int findSetAndPathCompression(int u) {
        if ( parents[u] != u ) {
            this->parents[u] = findSetAndPathCompression(parents[u]); 
        }
        return parents[u]; 
    }

    void unionByRank(int u, int v) {
        int u_parent = findSetAndPathCompression(u); 
        int v_parent = findSetAndPathCompression(v); 

        // Case 1: If they share the same father
        if (u_parent == v_parent) 
            return; 
        
        // Case 2: If they have different fathers
        if (rank[u_parent] > rank[v_parent]) {
            parents[v_parent] = u_parent; 
        } else if (rank[u_parent] < rank[v_parent]) {
            parents[u_parent] = v_parent; 
        } else {
            // choose either one
            parents[v_parent] = u_parent; 
            rank[v_parent]++; 
        }
    }

    vector<int> unionByRank_find_redundant(int u, int v) {
        vector<int> redundant; 
        int u_parent = findSetAndPathCompression(u); 
        int v_parent = findSetAndPathCompression(v); 

        // Case 1: If they share the same father
        if (u_parent == v_parent) {
            redundant.push_back(u); 
            redundant.push_back(v); 
            return redundant; 
        }
        
        // Case 2: If they have different fathers
        if (rank[u_parent] > rank[v_parent]) {
            parents[v_parent] = u_parent; 
        } else if (rank[u_parent] < rank[v_parent]) {
            parents[u_parent] = v_parent; 
        } else {
            // choose either one
            parents[v_parent] = u_parent; 
            rank[v_parent]++; 
        }
        return redundant; 
    }
}; 



class Solution {
public:
    // Leetcode 684. Redundant Connection
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int N = edges.size(); 
        Union_by_rank UF; 
        for (int i = 0; i < N + 1; i++) {
            UF.parents.push_back(i); 
        }
        for (int i = 0; i < N + 1; i++) {
            UF.rank.push_back(0); 
        }

        vector<vector<int>> redundent_ege; 

        for (vector<int> edge : edges) {
            int u = edge[0]; 
            int v = edge[1]; 

            vector<int> potential = UF.unionByRank_find_redundant(u, v); 
            if (potential.size()) {
                redundent_ege.push_back(potential); 
            }
        }

        return redundent_ege.back();         
    }

};


int main() {
    Solution solution; 

    // Leetcode 684. Redundant Connection
    vector<vector<int>> edges; 
    edges.push_back({1,2}); 
    edges.push_back({1,3}); 
    edges.push_back({2,3}); 
    vector<int> redundant = solution.findRedundantConnection(edges); 
    cout << "[" << redundant[0] << ", " << redundant[1] << "]"; 


    return 0;
}














