"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= MST Algorithm =========================================================
Prim class
Leetcode time


"""

from typing import List
from collections import defaultdict, deque
import heapq

class Prims:
    def __init__(self, graph: defaultdict(list), V: int):
        self.graph = graph  # Directed graph: node -> list of (neighbors, weight)
        self.V = V          # Number of vertices
        self.visited = [False] * V
        self.heap = []

    def mst(self, start: int) -> bool:
        numEdges = self.V - 1           # avoid cycle
        edgeCount, mstCost = 0, 0
        mstEdges = [None] * numEdges
        self.addEdge(start)

        # greedy algorithms: keep looking at the "cheapest" out-going edge
        while self.heap and edgeCount != numEdges:
            weight, nodeIndex, neighborIndex = heapq.heappop(self.heap)

            # node is already included in our MST
            if self.visited[neighborIndex]:
                continue
            
            # add this edge (node - > neighbor with weight of "weight")
            mstEdges[edgeCount] = (nodeIndex, neighborIndex, weight)
            edgeCount += 1
            mstCost += weight

            self.addEdge(neighborIndex)

        # if the heap runs out before we can get numEdges of edges, that means no MST is available
        if edgeCount != numEdges:
            return (None, None)
        
        print(mstCost)
        print(mstEdges)
        return (mstCost, mstEdges)



    def addEdge(self, nodeIndex: int):
        # Mark the current node as visited
        self.visited[nodeIndex] = True

        # Iterate over all edges going outwards from the current node
        # Add edges to the PQ which point to unvisited nodes
        neighborEdges = self.graph[nodeIndex]
        for neighbor in neighborEdges:
            neighborIndex, weight = neighbor
            if not self.visited[neighborIndex]:
                heapq.heappush(self.heap, (weight, nodeIndex, neighborIndex))

        

        



# Leetcode time
# class Solution: 
    # Leetcode 





if __name__ == "__main__":    
    # Example usage
    V = 8                                  # Number of vertices
    graph = defaultdict(list)
    graph[0] = [(1,10), (2,1), (3,4)]
    graph[1] = [(0,10), (2,3), (4,0)]
    graph[2] = [(0,1), (1,3), (5,8), (3,2)]
    graph[3] = [(0,4), (2,2), (5,2), (6,7)]
    graph[4] = [(1,0), (5,1), (7,8)]
    graph[5] = [(2,8), (4,1), (6,6), (7,9)]
    graph[6] = [(3,7), (5,6), (7,12)]
    graph[7] = [(4,8), (5,9), (6,12)]
    
    mstPrim = Prims(graph = graph, V = 8)
    mstPrim.mst(0)
    

    # =====================================================================
    # leetcode = Solution()
    



