"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= MST Algorithm =========================================================
Kruskals class - use UF
    1. Sort all edges by weight
    2. Walk through the sorted edges and look at the two nodes the edge belongs to
        If the nodes are already unified (same father), we don't include this case. Otherwise, we include it and unify the nodes
    3. The algorithm terminates when every edge has been processed or all the vertices have been unified

Leetcode time
    Leetcode 1584. Min Cost to Connect All Points

"""

from typing import List
from collections import defaultdict, deque

class Kruskals:
    pass





# Leetcode time
class Solution: 
    # Leetcode 1584. Min Cost to Connect All Points
    def minCostConnectPointsKruskal(self, points: List[List[int]]) -> int:
        V = len(points)
        mstNumEdge = V-1                    # our MST will have V-1 number of edges to avoid cycle
        edgeCount, mstCost = 0, 0
        edges = []                          # include (weight, u, v)
        parents = {i:i for i in range(len(points))}

        # -----------------------------------
        def findParents(x):
            if parents[x] != x:
                parents[x] = findParents(parents[x])
            return parents[x]

        # Return True if successfully union two nodes
        # Return False if two nodes already share the same parent
        def union(x, y):
            parentX, parentY = findParents(x), findParents(y)
            if parentX == parentY:
                return False

            parents[parentX] = parentY
            return True
           
        def computeWeight(xi, yi, xj, yj) -> int:
            return abs(xi-xj) + abs(yi-yj)
        # -----------------------------------

        # Graph representation: connect all nodes to all nodes -> V^2 edges
        # Cannot optimized like Prim's algo because here we need to sort all edges upfront
        for i in range(V):
            xi, yi = points[i]
            for j in range(i+1, V):
                xj, yj = points[j]
                weight = computeWeight(xi, yi, xj, yj)
                edges.append((weight, i, j))
                # edges.append((weight, j, i))

        # Sort all edges
        edges.sort()
        currentIndex = 0

        # Process each edge with increasing weight
        while edgeCount != mstNumEdge and currentIndex < len(edges):
            w, u, v = edges[currentIndex]

            if union(u, v):
                mstCost += w
                edgeCount += 1

            currentIndex += 1

        return mstCost





if __name__ == "__main__":    


    # =====================================================================
    # leetcode = Solution()
    



