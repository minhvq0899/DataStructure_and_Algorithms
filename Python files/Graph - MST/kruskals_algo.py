"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Topological Sorting Algorithm =========================================================
TopologicalSorting class
Leetcode time
    1. Leetcode 207:
    2. Leetcode 210:
    3. Leetcode 269: 
    4. Leetcode 310: 
    5. Leetcode 444:
    6. Leetcode 1136:

"""

from typing import List
from collections import defaultdict, deque

class Kruskals:
    def __init__(self, graph: defaultdict(list), V: int):
        self.graph = graph  # Directed graph: node -> list of neighbors
        self.V = V          # Number of vertices

    def mst(self) -> bool:




# Leetcode time
# class Solution: 
    # Leetcode 





if __name__ == "__main__":    
    # Example usage
    V = 14                                  # Number of vertices
    graph = defaultdict(list)
    graph[0] = [2,3]
    graph[1] = [4]
    graph[2] = [6]
    graph[3] = [1,4]
    graph[4] = [5,8]
    graph[6] = [7,11, 0]
    graph[7] = [4,12]
    graph[9] = [2,10]
    graph[10] = [6]
    graph[11] = [12]
    graph[12] = [8]

    ts = TopologicalSorting(graph, V)

    print(ts.kahn())
    
    
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
    



