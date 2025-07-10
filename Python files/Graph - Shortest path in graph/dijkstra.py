"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Dijkstra Algorithm =========================================================
Dijkstra class
Leetcode time
    1. Leetcode 743. Network Delay Time
    2. Leetcode 787. Cheapest Flights Within K Stops

"""
import heapq
from typing import List
import collections

# Dijkstra class
class Dijkstra:
    def __init__(self, graph: List[List[tuple]], dist: List[float], path: List[int]):
        self.graph = graph
        self.dist = dist # distance from s to all edges
        self.path = path

    def dijkstra(self, s: int):
        minHeap = []
        self.dist[s] = 0 # distance from s to s is 0
        heapq.heappush( minHeap, (0, s) )
        # when heap is not empty
        while minHeap:
            u = heapq.heappop(minHeap)
            uWeight, uID = u
            # check all adjacents of u[0]
            # v has the form of [v, weight]
            for v in self.graph[uID]:
                vID, vWeight = v
                # if s->u + u-> v  <  s->v
                # relax edge
                if uWeight + vWeight < self.dist[vID]:
                    self.dist[vID] = uWeight + vWeight
                    self.path[vID] = uID
                    heapq.heappush(minHeap, (uWeight + vWeight, vID))

class Dijkstra_787:
    def __init__(self, graph: collections.defaultdict(list), n: int, maxNumStops: int):
        self.graph = graph
        inf = float('inf')
        self.distances = [inf for _ in range (n)] 
        self.paths = [None for _ in range (n)]
        self.maxNumStops = maxNumStops

    def dijkstra(self, start: int, dst: int):
        self.distances[start] = 0
        self.paths[start] = start
        hq = [] # This heap will contain (distance, path, # of stops)
        heapq.heappush( hq, (self.distances[start], self.paths[start], -1) )

        while hq:
            u = heapq.heappop(hq)
            weight_u, vertice_u, numStops = u
            if vertice_u == dst:
                return weight_u
            for neighbor in self.graph[vertice_u]:
                v, weight_v = neighbor
                if weight_u + weight_v < self.distances[v] and numStops + 1 <= self.maxNumStops:
                    self.distances[v] = weight_u + weight_v
                    self.paths[v] = vertice_u
                    heapq.heappush( hq, (weight_u + weight_v, v, numStops + 1) )

# Leetcode time
class Solution: 
    # Leetcode 743. Network Delay Time
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # initialize graph and dist
        graph = [[] for _ in range(n+1)]
        for time in times:
            u, v, weight = time
            graph[u].append( (v, weight) )
        
        inf = float('inf')
        dist = [inf for _ in range (n+1)]
        
        # dijkstra
        minHeap = []
        dist[k] = 0 # dist from k to k is 0
        heapq.heappush( minHeap, (0, k) )
        while minHeap:
            u = heapq.heappop(minHeap)
            uWeight, uID = u
            for v in graph[uID]:
                vID, vWeight = v
                if uWeight + vWeight < dist[vID]:
                    dist[vID] = uWeight + vWeight
                    heapq.heappush( minHeap, (uWeight + vWeight, vID) )
        
        # Loop through dist
        maxDist = 0
        for d in dist[1:]:
            if d == float('inf'):
                return -1
            else: 
                maxDist = max(maxDist, d)
        
        return maxDist

        # Time: O(len(times) * log(n))
        # Space: O( len(time) + n )


    # ----------------------------------------------------------------------------------------------------
    # Leetcode 787. Cheapest Flights Within K Stops
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # ========== Step 1: Build the graph ==========
        # Create an adjacency list where graph[u] = list of (v, cost) pairs
        graph = [[] for _ in range(n)]
        for u, v, weight in flights:
            graph[u].append((v, weight))

        # ========== Step 2: Initialize distance tracking ==========
        # Each entry in dist[v] will store the minimum cost to reach node v
        # You could also track stops here, but it's not strictly necessary
        inf = float('inf')
        dist = [(inf, inf) for _ in range(n)]  # Optional: not used in logic below

        # ========== Step 3: Priority queue for modified Dijkstra ==========
        # Each heap entry is a tuple: (total_cost, current_node, stops_used)
        # We use a min-heap to always expand the cheapest path first
        minHeap = []
        heapq.heappush(minHeap, (0, src, 0))  # Start from src with cost 0 and 0 stops

        while minHeap:
            uWeight, uID, uStop = heapq.heappop(minHeap)

            # If we reach the destination, return the cost immediately
            if uID == dst:
                return uWeight

            # If we haven't exceeded the stop limit, explore neighbors
            if uStop <= K:
                for vID, vWeight in graph[uID]:
                    # Push the neighbor into the heap with updated cost and stop count
                    heapq.heappush(minHeap, (uWeight + vWeight, vID, uStop + 1))

        # If we exhaust the heap without reaching dst within K stops, return -1
        return -1

            # Time: O(V^2 log(V))
            # Space: O(V^2)





if __name__ == "__main__":
    """
    edges = [
            [0, 2, 1],
            [0, 1, 2],
            [0, 6, 3],
            [1, 5, 10],
            [1, 4, 15],
            [2, 1, 4],
            [2, 3, 2],
            [3, 4, 3],
            [4, 5, 5],
            [6, 1, 3] ]
            
    V = 7

    # our graph: graph[u] represents all adjacent vertices of u and their weight
    graph = [[] for _ in range (V)]
    for edge in edges:
        u, v, weight = edge
        graph[u].append((v, weight))

    inf = float('inf')
    dist = [inf for _ in range (V)]
    path = [-1 for _ in range(V)]
    s = 0 # find shortest path from 0 to all other vertices

    # create Dijkstra
    dijkstra_obj = Dijkstra(graph, dist, path)
    dijkstra_obj.dijkstra(s) # check shortest path from 0 to all edges
    print(dijkstra_obj.dist)
    """

    # =====================================================================
    leetcode = Solution()
    
    # -----------------------------------------------
    # maxDist = leetcode.networkDelayTime( [[2,1,1],[2,3,1],[3,4,1]], 4, 2 )
    # print(maxDist)
    
    # -----------------------------------------------
    minPrice = leetcode.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
    print(minPrice)



