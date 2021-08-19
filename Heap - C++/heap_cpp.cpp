/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Heap =========================================================
1) Leetcode 692. Top K Frequent Words
2) Leetcode 23. Merge k Sorted Lists
3) Leetcode 973. K Closest Points to Origin

*/ 

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <bits/stdc++.h>
#include <string>
#include <tuple>
using namespace std;

class Solution {
public:
    // Leetcode 692. Top K Frequent Words
    struct compare {
        bool operator() (const pair<int, string>& a, const pair<int, string>& b) {
            if(a.first != b.first) 
                return a.first > b.first;              
            else 
                return a.second < b.second;         
            
        }
    };

    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freq; 
        for (string word : words) {
            freq[word]++; 
        }

        // pq
        priority_queue <pair<int, string>, vector<pair<int, string>>, compare> heap; 

        for (auto x : freq) {
            heap.push( {x.second, x.first} ); 
            if (heap.size() > k) {
                heap.pop(); 
            }
        }

        vector<string> result; 
        while (k > 0) {
            result.push_back(heap.top().second); 
            heap.pop(); 
            k--; 
        }

        reverse(result.begin(), result.end()); 
        return result; 
    }




    // ======================================================================================================================
    // Leetcode 23. Merge k Sorted Lists
    struct ListNode {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

    class compare23 {
    public:
        int operator() (ListNode* n1, ListNode* n2) {
            return n1->val > n2->val; 
        }
    }; 

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue <ListNode*, vector<ListNode*>, compare23> min_heap; 

        // insert all list nodes in the min heap: O(k) with k is the length of list
        for (ListNode* node : lists) {
            if (node) min_heap.push(node); 
        }

        // create a new list
        ListNode* dummy = new ListNode(); 
        ListNode* current = dummy; 
        while (!min_heap.empty()) {                 // O(n) with n is the total number of node in all k node* 
            ListNode* node = min_heap.top();        // O(1)
            min_heap.pop();                         // O(log(k))
            current->next = node;
            current = current->next;
            if (node && node->next) {               
                min_heap.push(node->next);          // O(log(k))
            }
        }

        return dummy->next; 
    }


    // ======================================================================================================================
    // Leetcode 973. K Closest Points to Origin
    class compare973 {
    public:
        int operator() (pair<double, int>& a, pair<double, int>& b) {
            return a.first > b.first; 
        }
    }; 
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        cout << sqrt(pow(1, 2) + pow(3, 2)) << "\n"; 
        
        priority_queue <pair<double, int>, vector<pair<double, int>>, compare973> min_heap; 
        
        for (int i = 0; i < points.size(); i++) {
            double x = points[i][0];
            double y = points[i][1];
            double distance = sqrt(pow(x, 2) + pow(y, 2)); 
            cout << distance << "\n";
            min_heap.push( {distance, i} ); 
        }
        
        vector<vector<int>> ans; 
        for (int c = 0; c < k; c++) {
            double dis = min_heap.top().first; 
            int index = min_heap.top().second; 
            min_heap.pop();
            ans.push_back(points[index]); 
        }
        
        return ans; 
    }


};


int main() {
    Solution solution; 

    // Leetcode 692. Top K Frequent Words -------------------------------------------------------------------
    // vector<string> words = {"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "is"}; 
    // vector<string> result = solution.topKFrequent(words, 4); 

    // for (string s: result) {
    //     cout << s << "  "; 
    // }


    // Leetcode 23. Merge k Sorted Lists -------------------------------------------------------------------


    return 0;
}














