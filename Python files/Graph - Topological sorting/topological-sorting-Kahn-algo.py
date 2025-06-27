"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Topological Sorting Algorithm =========================================================
TopologicalSorting class
Leetcode time
    1. Leetcode 207:
    2. Leetcode 210. Course Schedule II
    3. Leetcode 269: 
    4. Leetcode 310: Minimum Height Trees
    5. Leetcode 444:
    6. Leetcode 1136:

"""

from typing import List
from collections import defaultdict, deque
import collections

class TopologicalSorting:
    def __init__(self, graph: defaultdict(list), V: int):
        self.graph = graph  # Directed graph: node -> list of neighbors
        self.V = V          # Number of vertices

    def kahn(self) -> bool:
        """Performs topological sorting using Kahn’s algorithm.
        Returns True if a valid sort exists (i.e., no cycle), False otherwise."""
        in_degree = [0] * self.V  # Tracks incoming edge count for each node

        # Step 1: Compute in-degree for each node
        for u in range(self.V):
            for v in self.graph[u]:
                in_degree[v] += 1

        print("Original in-degree array: ", in_degree)

        # Step 2: Initialize queue with all nodes having in-degree 0
        queue = deque([i for i in range(self.V) if in_degree[i] == 0])
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1  # Remove edge u → v
                if in_degree[v] == 0:
                    queue.append(v)

        # If we processed all nodes, we have a valid topological ordering
        if len(topo_order) == self.V:
            print("Topological Order:", topo_order)
            return True
        else:
            print("Cycle detected. No valid topological ordering.")
            print("Incorrect topo order: ", topo_order)
            return False
        

        




class Solution: 
    # Leetcode 210. Course Schedule II --------------------------------------------------------------------------------------------
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Going to use Kahn's algo for Topo sorting"""
        # Step 1: Create graph and in_degree list for all nodes
        graph = collections.defaultdict(list)
        in_degree = [0 for _ in range (numCourses)]
        for pre in prerequisites:
            a, b = pre
            graph[b].append(a)
            in_degree[a] += 1

        # Step 2: Initialize a queue with all nodes having in-degree of 0
        queue = collections.deque( [i for i in range (numCourses) if in_degree[i] == 0] )
        #print(queue)

        # Step 3: Repreatedly remove node from the graph until all nodes are processed
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for neighbor in graph[u]:
                in_degree[neighbor] -= 1        # remove edge u -> neighbor
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        print(topo_order)

        if len(topo_order) == numCourses:
            return topo_order
        
        return []  


    # Leetcode 310: Minimum Height Trees --------------------------------------------------------------------------------------------
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Corner case
        if n == 1:
            return [0]
        
        # Step 1: Create a undirected graph. in_degree can be inferred from the graph
        graph = defaultdict(set)
        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)

        # Step 2: Initialize a queue with all the leave nodes
        queue_leaves = deque( [i for i in range (n) if len(graph[i]) == 1] )
        numNodes = n

        # Step 3: Trim leaves
        while numNodes > 2:
            numLeaves = len(queue_leaves)
            numNodes -= numLeaves                       # After trimming all leaves
            
            print(queue_leaves)
            for _ in range (len(queue_leaves)):
                leaf = queue_leaves.popleft()
                neighbor = graph[leaf].pop()            # graph[leaf] should only have one element left
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    queue_leaves.append(neighbor)
        
        # print(queue_leaves)
        return list(queue_leaves)
 





if __name__ == "__main__":    
    """
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
    # =====================================================================
    leetcode = Solution()

    # Leetcode 310: Minimum Height Trees --------------------------------------------------------------------------------------------
    edges = [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[6,8],[8,9],[9,10]]
    answer310 = leetcode.findMinHeightTrees(11, edges)
    print(answer310)



