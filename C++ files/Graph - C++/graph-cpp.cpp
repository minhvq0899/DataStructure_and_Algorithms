/*
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Graph =========================================================
1) Leetcode 797. All Paths From Source to Target
2) Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero
3) Leetcode 133. Clone Graph
4) Leetcode 785. Is Graph Bipartite?
5) Leetcode 743. Network Delay Time
6) Leetcode 1042. Flower Planting With No Adjacent

*/ 

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <limits>
using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Dijkstra {
public:
	vector<vector<pair<int, int>>>& graph; 
	vector<int>& distance; 
	vector<int>& path; 
	Dijkstra(vector<vector<pair<int, int>>>& _graph, vector<int>& _distance, vector<int>& _path) : graph(_graph), distance(_distance), path(_path) {}

    struct compare {
        bool operator() (const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second;         
        }
    };

	void dijkstra_algo(int s) {
		priority_queue <pair<int, int>, vector<pair<int, int>>, compare> min_heap; 
		distance[s] = 0; 			
		min_heap.push( {s, 0} ); 

		while (!min_heap.empty()) {
			int uID = min_heap.top().first; 
            int uWeight = min_heap.top().second; 
			min_heap.pop(); 
			for (auto v: graph[uID]) {
                int vID = v.first; 
                int vWeight = v.second; 
				if (uWeight + vWeight < distance[vID]) {
					distance[vID] = uWeight + vWeight;
					min_heap.push( {vID, uWeight + vWeight} ); 
				}
			}
		}
	}
};

class Solution {
public:
    // vector<bool> visited (graph.size(), false); 
    // vector<int> path (graph.size(), -1);

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



    // ================================================================================================================================================================================================================
    // Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero
    int minReorder(int n, vector<vector<int>>& connections) {
        // set up graph
        vector<vector<int>> graph (n, vector<int>());
        // neighbor list
        vector<vector<int>> neighbor_list (n, vector<int>()); 
        for (vector<int> con : connections) {
            int u = con[0]; 
            int v = con[1]; 
            graph[u].push_back(v); 
            neighbor_list[u].push_back(v); 
            neighbor_list[v].push_back(u); 
        }
        // reachable list
        vector<bool> reachable_0 (n, false); 
        reachable_0[0] = true;  // you can reach to 0 from 0

        // dfs
        int change = 0; 
        stack<int> s; 
        s.push(0); 
        while (!s.empty()) {
            int u = s.top();
            s.pop(); 
            for (int v : neighbor_list[u]) {
                if (!reachable_0[v]) {
                    reachable_0[v] = true; 
                    s.push(v); 
                    if ( (find(graph[v].begin(), graph[v].end(), 0) == graph[v].end()) && (find(graph[v].begin(), graph[v].end(), u) == graph[v].end()) ) {
                        change++; 
                    }
                }
            }
        }

        return change; 
    }



    // ================================================================================================================================================================================================================
    // Leetcode 133. Clone Graph
    Node* cloneGraph(Node* node) {
        if (!node) return NULL; 
        queue<Node*> queue;              // for bfs
        unordered_map<Node*, Node*> map; // store the deep copy of each vertice
        map[node] = new Node(node->val); 
        
        unordered_set<int> visited;      // store the visited vertices
        visited.insert(node->val); 
        
        // bfs
        queue.push(node); 
        while (!queue.empty()) {
            Node* u = queue.front();
            queue.pop(); 
            
            for (Node* v : u->neighbors) {
                if (map.find(v) == map.end()) {
                    map[v] = new Node(v->val); 
                }
                // create connection
                map[u]->neighbors.push_back(map[v]); 
                // add v to visited list
                if (visited.find(v->val) == visited.end()) {
                    visited.insert(v->val); 
                    queue.push(v);
                }
            }
        } 
        
        return map[node];  
    }

    


    // ================================================================================================================================================================================================================
    // Leetcode 785. Is Graph Bipartite?
    bool bfs785(vector<vector<int>>& graph, int start) {
        vector<int> visited (graph.size(), 0); 

        // bfs
        queue<int> queue; 
        visited[start] = 1; 
        queue.push(start); 

        int u;
        while (!queue.empty()) {
            u = queue.front(); 
            queue.pop(); 
            for (int v: graph[u]) {
                if (visited[v] == 0) {
                    visited[v] = visited[u] * (-1); 
                    queue.push(v);
                } else if (visited[v] == visited[u]) {
                    return false; 
                }
            }
        }
        return true;
    }
    
    bool isBipartite(vector<vector<int>>& graph) {
        int num_true = 0; 
        for (int i = 0; i < graph.size(); i++) {
            if (bfs785(graph, i)) num_true++; 
        }

        return num_true == graph.size(); 
    }



    // ================================================================================================================================================================================================================
    // Leetcode 743. Network Delay Time
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> graph (n+1);
        vector<int> distance (n+1, INT_MAX); 
        vector<int> path (n+1, -1); 

        for (vector<int> edge : times) {
            int u = edge[0]; 
            int v = edge[1]; 
            int weight = edge[2]; 
            graph[u].push_back( {v, weight} ); 
        } 

        Dijkstra dijkstra_obj (graph, distance, path); 
        dijkstra_obj.dijkstra_algo(k); 

        // Loop through distance
        int max_dist = 0; 
        for (int i = 1; i < dijkstra_obj.distance.size(); i++) {
            if (dijkstra_obj.distance[i] == INT_MAX) {
                return -1; 
            } else {
                max_dist = max(max_dist, dijkstra_obj.distance[i]); 
            }
        }
        
        return max_dist; 
    }


    // ================================================================================================================================================================================================================
    // Leetcode 1042. Flower Planting With No Adjacent
    vector<int> gardenNoAdj(int n, vector<vector<int>>& paths) {
        vector<vector<int>> graph (n + 1, vector<int>());

        for (vector<int> path : paths) {
            int v1 = path[0]; 
            int v2 = path[1]; 
            graph[v1].push_back(v2);
            graph[v2].push_back(v1); 
        }

        unordered_map<int, int> flower_map; 
        for (int i = 1; i < n+1; i++) {
            unordered_set<int> flower_types ({1,2,3,4}); 
            vector<int> connecting_edges = graph[i]; 

            for (int con_edge : connecting_edges) {
                if (flower_map[con_edge] != 0) {
                    flower_types.erase(flower_map[con_edge]);
                }
            }

            for (int k = 1; k < 5; k++) {
                if (flower_types.find(k) != flower_types.end()) {
                    flower_types.erase(k); 
                    flower_map[i] = k; 
                    break; 
                }
            }
        }

        vector<int> ans (n, 0);  
        for (auto kv : flower_map) {
            ans[kv.first - 1] = kv.second; 
        }

        return ans; 
    }

};


int main() {
    Solution solution; 

    // Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero
    // int n = 6; 
    // vector<vector<int>> connections;  // [[0,1],[1,3],[2,3],[4,0],[4,5]]
    // connections.push_back({0, 1}); 
    // connections.push_back({1, 3}); 
    // connections.push_back({2, 3}); 
    // connections.push_back({4, 0});
    // connections.push_back({4, 5}); 
    // cout << solution.minReorder(n, connections); 

    // 

    return 0;
}














