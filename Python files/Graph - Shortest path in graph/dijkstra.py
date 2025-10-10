"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Dijkstra Algorithm =========================================================
Find shortest path
    non-weighted -> BFS
    weighted -> Dijkstra

Dijkstra's limitation: won't work if the graph has a cycle with negative weight

Condition of the Graph for Dijkstra to work:
    directed -> no cycle with negative weight
        A -> B : negative 
            neu e muon xai lai cai directed edge nay, thi e cung fai di B -> C ... -> A
            Khi em quay lai A, thi e moi xai lai A -> B
            Gia su A -> B -> C -> ... -> A : duong di nay co cai total weight > 0
                Minh khong muon lap di lap lai cai cycle nay, boi vi moi lan minh lap cai cycle nay thi cai cost cua minh no se tang len infinitely
    non-directed -> no negative weight edge because each edge is a cycle itself (a <-> b)

Implementation:
    Dijkstra use heap
    Time complexity: O(ElogV)

Insight:
    1. In Dijkstra, after adding new tuple (distance 'start' -> node, node index) into our heap, naturally we will process these distances from smallest 
    dist to largest dist. As a result, once a node is popped from the heap, its shortest distance from the start is finalized. 
    After that, no future entry for that node will have a smaller distance — because all shorter paths would have already been processed.
    Ex: heap = [(2, A), (5, A)]
    - You pop (2, A) → finalize A with distance 2.
    - Later, (5, A) is still in the heap, but you skip it because A is already finalized

    2. In Dijkstra’s algorithm, if you pop a node with a weight greater than its current recorded distance, 
    it means that node was already processed with a better path. This is expected and does not imply a negative cycle.

    3. Dijkstra's algo gives us the shortest distances from one 'start' node to EVERY OTHER nodes.
    However, in problem where we only need to compute the shortest dist from 'start' to ONE NODE 'end',
    we can stop our while loop once the popped node is the 'end' node
    Ex: 
    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if node == end:
            return dist  # Done!    

Leetcode time
    Leetcode 743. Network Delay Time (2 solutions)
    Leetcode 1514. Path with Maximum Probability
    Leetcode 787. Cheapest Flights Within K Stops
    Leetcode 505. The Maze II
    Leetcode 3341. Find Minimum Time to Reach Last Room I

"""


import heapq
from typing import List
import collections
import bisect

# Dijkstra class
class Dijkstra:
    def __init__(self, graph: List[List[tuple]], n: int):
        self.graph = graph
        # Distance from s to all edges. Initialized as INF
        inf = float('inf')
        self.dist = [inf for _ in range(n)]              
        self.path = [i for i in range(n)]

    def dijkstra(self, s: int):
        minHeap = []
        self.dist[s] = 0                # distance from s to s is 0
        heapq.heappush( minHeap, (0, s) )

        while minHeap:
            uWeight, uID = heapq.heappop(minHeap)
            # check all neighbors
            # v has the form of [vID, vWeight]
            for vID, vWeight in self.graph[uID]:
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

    # Anh Quang's solution
    # Applying insight #1
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        # Graph representation
        graph = collections.defaultdict(list)               # v -> [[u, weight], [], ...]
        for u, v, weight in times:
            graph[u].append([v, weight])
        
        result = 0
        heap = [(0, k)]
        heapq.heapify(heap)

        # In this problem, we are assuming the weight of an edge is non-negative because according to the problem description,
        # "w is the time it takes for a signal to travel from source to target"
        # So 'visited' can just be a set (applying insight #1). However, for the sake of learning, in the case edge weight can be
        # negative, we can check for existence of negative weighted cycle like below
        visited = collections.defaultdict(int)

        while heap and len(visited) < n:
            currentWeight, currentNode = heapq.heappop(heap)
            if currentNode in visited:
                if currentWeight < visited[currentNode]: # co negative cycle
                    return -1
                continue
            visited[currentNode] = currentWeight
            result = currentWeight
            for dest, weight in graph[currentNode]:
                if dest not in visited:
                    heapq.heappush(heap, (currentWeight + weight, dest))
        
        if len(visited) == n: 
            return result
        return -1

    # ----------------------------------------------------------------------------------------------------
    # Leetcode 1514. Path with Maximum Probability
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # graph representation
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            weight = succProb[i]
            graph[u].append([v, -weight])
            graph[v].append([u, -weight])

        # dijkstra algo
        distances = collections.defaultdict(float)
        for i in range(n):
            distances[i] = float('-inf')
        distances[start_node] = 1

        heap = [(-1, start_node)]               # negate the prob in heap because it's a min-heap
        heapq.heapify(heap)

        while heap:
            prob, v = heapq.heappop(heap)

            # Insight #3
            if v == end_node:
                return -prob
                
            for neighborV, neighborW in graph[v]:
                # Relaxation
                new_prob = prob * neighborW
                if new_prob > distances[neighborV]:
                    distances[neighborV] = new_prob
                    heapq.heappush(heap, (-new_prob, neighborV))

        # print(distances)

        return distances[end_node] if distances[end_node] != float('-inf') else 0
        

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
    
    # ----------------------------------------------------------------------------------------------------
    # Leetcode 505. The Maze II
    # For LC490 we can use DFS with 'visited' set because we only have to check if it's possible to reach the destination.
    # However, for this LC 505, DFS with 'visited' set can potentially skip shorter paths if a longer one already reached a node first.
    # We cannot use BFS either because each edge has a different weight. BFS would work if we want the path with the minimum hops (each hop has weight of 1).
    # For this problem, we need to use Dijkstra.
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # -------------------------------------------------
        def computeDistance(rStart, cStart, rEnd, cEnd) -> int:
            if rStart == rEnd:
                return abs(cStart - cEnd)
            else:
                return abs(rStart - rEnd)
        # -------------------------------------------------
        rowLen = len(maze)
        colLen = len(maze[0])
        wallsIdxForEachRow = [[] for _ in range(rowLen)]
        wallsIdxForEachCol = [[] for _ in range(colLen)]

        # Data Structures for our Dijkstra algo
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))           # (distance, r, c)
        distances = collections.defaultdict(int)                # shortest distance from 'start' to each node
        distances[(start[0], start[1])] = 0

        # Populate our ds
        for r in range(rowLen):
            for c in range(colLen):
                # Populate 'wallsIdxForEachRow' and 'wallsIdxForEachCol'
                if maze[r][c] == 1:
                    wallsIdxForEachRow[r].append(c)
                    wallsIdxForEachCol[c].append(r)
                # Populate our 'distances' dict
                else:
                    if r != start[0] or c != start[1]:
                        distances[(r,c)] = float('inf')

        # print(wallsIdxForEachCol)
        # print(wallsIdxForEachRow)

        # DFS traversal
        while heap:
            d, pr, pc = heapq.heappop(heap)
            # Now roll the ball all the way to up, right, down, left until we hit a wall
            # Roll in 4 directions
            # Roll up
            up_idx = bisect.bisect_left(wallsIdxForEachCol[pc], pr)
            upR = wallsIdxForEachCol[pc][up_idx - 1] + 1 if up_idx > 0 else 0
            upC = pc

            # Roll down
            down_idx = bisect.bisect_right(wallsIdxForEachCol[pc], pr)
            downR = wallsIdxForEachCol[pc][down_idx] - 1 if down_idx < len(wallsIdxForEachCol[pc]) else rowLen - 1
            downC = pc

            # Roll left
            left_idx = bisect.bisect_left(wallsIdxForEachRow[pr], pc)
            leftC = wallsIdxForEachRow[pr][left_idx - 1] + 1 if left_idx > 0 else 0
            leftR = pr

            # Roll right
            right_idx = bisect.bisect_right(wallsIdxForEachRow[pr], pc)
            rightC = wallsIdxForEachRow[pr][right_idx] - 1 if right_idx < len(wallsIdxForEachRow[pr]) else colLen - 1
            rightR = pr

            # Check each neighbor node
            for nextR, nextC in [(upR, upC), (rightR, rightC), (downR, downC), (leftR, leftC)]:
                edgeWeight = computeDistance(pr, pc, nextR, nextC)
                newShortestDist = distances[(pr, pc)] + edgeWeight
                if newShortestDist < distances[(nextR, nextC)]:
                    distances[(nextR, nextC)] = newShortestDist
                    heapq.heappush(heap, (newShortestDist, nextR, nextC))

        return distances[(destination[0], destination[1])] if distances[(destination[0], destination[1])] != float('inf') else -1


    # ----------------------------------------------------------------------------------------------------
    # Leetcode 3341. Find Minimum Time to Reach Last Room I
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        graph = collections.defaultdict(list)       # List[List[tuple]]
        rowLen = len(moveTime)
        colLen = len(moveTime[0])
        startTime = moveTime[0][0]
        # ----------------------------
        def computeNodeIndex(row, col) -> int:
            return row * colLen + col
        # ----------------------------

        # Graph representation
        for r in range(rowLen):
            for c in range(colLen):
                nodeIndex = computeNodeIndex(r, c)
                nodeTimestamp = moveTime[r][c]
                for deltaR, deltaC in [(-1, 0), (0, 1), (1, 0), (0, -1)]:       # up, right, down, left
                    nextR = r + deltaR
                    nextC = c + deltaC
                    if 0 <= nextR < rowLen and 0 <= nextC < colLen:
                        neighborIndex = computeNodeIndex(nextR, nextC)
                        neighborTimestamp = moveTime[nextR][nextC]
                        edgeWeight = 1 + abs(neighborIndex-nodeIndex)
                        if neighborTimestamp > nodeTimestamp:
                            graph[neighborIndex].append((nodeIndex, 1))
                            graph[nodeIndex].append((neighborIndex, edgeWeight))
                        else:
                            graph[neighborIndex].append((nodeIndex, edgeWeight))
                            graph[nodeIndex].append((neighborIndex, 1))

        # print(graph)

        # Run Dijkstra - start from cell (0,0)
        inf = float('inf')
        dist = [inf for _ in range(rowLen*colLen)]       
        dist[0] = 0 
        minHeap = []
        heapq.heappush(minHeap, (0,0))

        while minHeap:
            uID, uWeight = heapq.heappop(minHeap)
            for vID, vWeight in graph[uID]:
                # Relaxation
                if uWeight + vWeight < dist[vID]:
                    dist[vID] = uWeight + vWeight
                    heapq.heappush(minHeap, (vID, uWeight + vWeight))

        # print(dist)
        return dist[computeNodeIndex(rowLen-1, colLen-1)] + startTime

                             





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
    # minPrice = leetcode.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
    # print(minPrice)

    # -----------------------------------------------
    # moveTime = [[0,4],[4,4]]
    # minTime = leetcode.minTimeToReach(moveTime)
    # print(minTime)

    # -----------------------------------------------
    maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
    start = [0,0]
    destination = [8,6]

    ans505 = leetcode.shortestDistance(maze, start, destination)
    print(ans505)

