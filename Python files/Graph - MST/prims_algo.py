"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= MST Algorithm =========================================================
Prims class

Leetcode time
    Leetcode 1135. Connecting Cities With Minimum Cost
    Leetcode 1584. Min Cost to Connect All Points
    Leetcode 1631. Path With Minimum Effort



"""

from typing import List
from collections import defaultdict
import heapq

class Prims:
    def __init__(self, graph: defaultdict(list), V: int):
        self.graph = graph                  # Directed graph: node -> list of (neighbors, weight)
        self.V = V                          # Number of vertices
        self.visited = [False] * (V+1)      # (V+1) for any problem that node labeled from 1->n. If it's labeled from 0->(n-1), then V should be sufficient
        self.heap = []

    def mst(self, start: int) -> bool:
        numEdges = self.V - 1           # avoid cycle
        edgeCount, mstCost = 0, 0
        mstEdges = [None] * numEdges
        self.addEdge(start)

        # greedy algorithms: keep looking at the "cheapest" out-going edge
        # if solution exists, this while loop runs for exactly E number of time. each time it runs heappop, which is log(E)
        # --> Time complexity: E * log(E)
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
class Solution: 
    # Leetcode 1135. Connecting Cities With Minimum Cost
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        # graph representation
        for conn in connections: 
            u, v, w = conn
            graph[u].append((v, w))
            graph[v].append((u, w))

        primsClass = Prims(graph, n)
        mstCost, mstEdges = primsClass.mst(1)

        return mstCost if mstCost != None else -1
        
    # -----------------------------------------------------------
    # Leetcode 1584. Min Cost to Connect All Points
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        # prepare weights and graph repre
        for i in range (len(points)):
            pointI = points[i]
            for j in range (i+1, len(points)):
                pointJ = points[j]
                weight = self.computeCost(pointI, pointJ)
                graph[i].append((j, weight))
                graph[j].append((i, weight))

        primsClass = Prims(graph, len(points))
        mstCost, mstEdges = primsClass.mst(0)

        return mstCost

    def computeCost(self, pointA: List[int], pointB: List[int]) -> int:
        Ax, Ay = pointA
        Bx, By = pointB

        return abs(Ax - Bx) + abs(Ay - By)
        
    
    # -----------------------------------------------------------
    # Leetcode 1631. Path With Minimum Effort
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        










if __name__ == "__main__":  
    """
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
    """

    # =====================================================================
    leetcode = Solution()

    # ----------------------------------------------------------
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(leetcode.minCostConnectPoints(points))
    



