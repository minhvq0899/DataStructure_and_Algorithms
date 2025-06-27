"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Bellman-Ford Algorithm =========================================================
Bellman-Ford class
Leetcode time
    1. Leetcode 1334: 

"""

from typing import List
import collections

# BellmanFord class
class BellmanFord:
    def __init__(self, graph: collections.defaultdict(list), V: int):
        self.graph = graph                  # Adjacency list representation: graph[u] = [(v, weight), ...]
        self.dist = [float("inf")] * V      # Distance from source to all vertices
        self.path = [-1] * V                # Stores the shortest path tree

    def bellman_ford(self, s: int, V: int) -> bool:
        """Find shortest paths from source 's' using Bellman-Ford. Detects negative cycles."""
        self.dist[s] = 0  # Distance from source to itself is 0

        # Step 1: Relax all edges (V-1) times
        for _ in range(V - 1):
            for u in range(V):
                if u in self.graph:
                    for vID, vWeight in self.graph[u]:  # For each neighbor (v, weight)
                        # Relaxation: Update distance if shorter path found
                        if self.dist[u] + vWeight < self.dist[vID]:
                            self.dist[vID] = self.dist[u] + vWeight
                            self.path[vID] = u  # Store previous node

        # Step 2: Check for negative-weight cycles
        for u in range(V):
            for vID, vWeight in self.graph[u]:
                if self.dist[u] + vWeight < self.dist[vID]:  # If still improving, cycle exists
                    print("Graph contains a negative-weight cycle.")
                    return False  # Algorithm fails due to cycle

        return True  # No negative cycle found, valid shortest paths




# Leetcode time
# class Solution: 
    # Leetcode 





if __name__ == "__main__":    
    # Example usage
    V = 6  # Number of vertices
    graph = collections.defaultdict(list)
    graph[0] = [(1, 5), (2, 35), (3, 40)]   # Edges from node 0
    graph[1] = [(4, 25), (3, 20)]           # Edges from node 1
    graph[2] = [(4, -30), (5, 30)]          # Edges from node 2
    graph[3] = [(5, 20)]                    # Edges from node 3
    graph[4] = [(5, 25)]                    # Edges from node 4

    bf = BellmanFord(graph, V)

    if bf.bellman_ford(0, V):  # Run Bellman-Ford from source 0
        print("Shortest distances:", bf.dist)
        print("Path:", bf.path)
    
    
    """

    V = 5  # Number of vertices
    graph = [
        [(1, 6), (2, 7)],  # Edges from node 0
        [(2, 8), (3, 5), (4, -4)],  # Edges from node 1
        [(3, -3), (4, 9)],  # Edges from node 2
        [(1, -2)],  # Edges from node 3
        [(0, 2), (3, 7)]  # Edges from node 4
    ]

    dist = [float("inf")] * V
    path = [-1] * V
    bf = BellmanFord(graph, dist, path)

    if bf.bellman_ford(0, V):  # Run Bellman-Ford from source 0
        print("Shortest distances:", dist)
        print("Path:", path)
    """

    # =====================================================================
    # leetcode = Solution()
    



