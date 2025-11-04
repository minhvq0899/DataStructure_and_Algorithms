"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Breadth First Search =========================================================

(Medium)
Leetcode 690. Employee Importance
Leetcode 1129. Shortest Path with Alternating Colors
Leetcode 752. Open the Lock
Leetcode 785. Is Graph Bipartite?
Leetcode 909. Snakes and Ladders
Leetcode 1091. Shortest Path in Binary Matrix
Leetcode 399. Evaluate Division
Leetcode 1730. Shortest Path to Get Food - Premium

    (Multi-source BFS)
Leetcode 542. 01 Matrix
Leetcode 1162. As Far from Land as Possible
Leetcode 994. Rotting Oranges
Leetcode 286. Walls and Gates

(Hard)
Leetcode 847. Shortest Path Visiting All Nodes - Generalized BFS
Leetcode 1293. Shortest Path in a Grid with Obstacles Elimination
Leetcode 127. Word Ladder
Leetcode 126. Word Ladder II
Leetcode 864. Shortest Path to Get All Keys

"""



from typing import List, Tuple
import queue
from collections import deque, defaultdict


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    # Leetcode 690. Employee Importance
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # to store the graph in format
        # {id: object}
        graph = {}
        for emp in employees:
            graph[emp.id] = emp
        
        # initialize a queue
        q = queue.Queue()
        q.put(id)
        
        # BFS
        count = graph[id].importance
        while q.qsize() > 0:
            u = q.get()
            vertices = graph[u].subordinates
            for v in vertices: # list of all subordinates of u
                q.put(v)
                count += graph[v].importance
        
        return count

    # -------------------------------------------------------------------
    # Leetcode 1129. Shortest Path with Alternating Colors
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # initialize BFS
        graph_red = [[] for _ in range (n)]
        for edge in red_edges:
            u, v = edge
            graph_red[u].append(v)
        graph_blue = [[] for _ in range (n)]
        for edge in blue_edges:
            u, v = edge
            graph_blue[u].append(v)
        
        visited = [[False, False] for _ in range (n)] # [[r, b], ...]
        dist = [float('inf') for _ in range (n)]
        dist[0] = 0
        q = queue.Queue()

        # BFS
        # mark that we have visited both red and blue start
        visited[0] = [True, True] 
        # put both red and blue start into queue
        q.put( (0, 0, 'r') )
        q.put( (0, 0, 'b') )

        # keep running while the queue is not empty
        while q.qsize() > 0:
            u = q.get() # pop the queue
            node, level, color = u

            if color == 'r':
                for v in graph_blue[node]:
                    if not visited[v][1]: 
                        visited[v][1] = True
                        dist[v] = min(dist[v], level+1)
                        q.put( (v, level+1, 'b') )

            if color == 'b':
                for v in graph_red[node]:
                    if not visited[v][0]:
                        visited[v][0] = True
                        dist[v] = min(dist[v], level+1)
                        q.put( (v, level+1, 'r') )
        
        # return answer
        for i in range (len(dist)):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist
    
        # E: số cạnh
        # V: số node
        # Time Complexity: O(E+V)
        # Extra Space Complexity: O(E) 

    # --------------------------------------------------------------------
    # Leetcode 752. Open the Lock
    def openLock(self, deadends: List[str], target: str) -> int:
        # if each time you checks for deadends, you have to iterates through a list, it will be O(n)
        # instead, store you deadends in a set
        deadendsSet = {deadend for deadend in deadends}

        # initialize BFS
        q = queue.Queue()
        visited = [False for _ in range (10000)]
        path = [-1 for _ in range (10000)]

        # BFS
        visited[0] = True # we start at "0000"
        q.put("0000")

        while q.qsize() > 0:
            u = q.get()
            if u not in deadendsSet:
                neighbors = self.find_neighbor(u) # neighbors is a list
                for neighbor in neighbors:
                    neighbor_int = int(neighbor)
                    if not visited[neighbor_int]:
                        visited[neighbor_int] = True
                        path[neighbor_int] = int(u)
                        q.put( neighbor )

        # return 
        if target == "0000" and target not in deadendsSet:
            return 0
            
        count = 0
        target_int = int(target)
        if path[ target_int ] != -1:
            while target_int != 0:
                target_int = path[target_int]
                count += 1
            return count

        return -1
        # V là số đỉnh -> có 10000 đỉnh, tương ứng với 10000 trường hợp từ 0000 -> 9999
        # E là số đỉnh -> có 80000 cạnh, mỗi đỉnh trung bình có 8 cạnh (trừ các đỉnh deadends)
        # Time Complexity: O(10000 + 80000)
        # Extra Space Complexity: O(10000)
                
    # u passed into this find_neighbor is definitely not in deadends
    def find_neighbor(self, current: str) -> List[str]:
        neighbors_list = []
        current = list(current)

        for i in range (len(current)):
            digit = int( current[i] )    
            if digit == 9:
                # go up
                current[i] = "0"
                neighbors_list.append( "".join(current) )
                # go down
                current[i] = "8"
                neighbors_list.append( "".join(current) )
                # restore
                current[i] = "9"
            elif digit == 0:
                # go up 
                current[i] = "1"
                neighbors_list.append( "".join(current) )
                # go down
                current[i] = "9"
                neighbors_list.append( "".join(current) )
                # restore
                current[i] = "0"
            else: 
                # go up
                current[i] = str( digit + 1 )
                neighbors_list.append( "".join(current) )
                # go down
                current[i] = str( digit - 1 )
                neighbors_list.append( "".join(current) )
                # restore
                current[i] = str(digit)

        return neighbors_list
    

    # --------------------------------------------------------------------
    # Leetcode 785. Is Graph Bipartite?
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Initialize DS
        visited = [0 for _ in range (len(graph))]       # visited can have 3 values: -1, 0, 1
        queue = deque([])

        # Initialize BFS from each unvisited node to cover all CC
        for node in range (len(graph)):
            # If we haven't visited node, add it to the queue and start bfs with color 1
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1

                while queue:
                    u = queue.popleft()
                    uColor = visited[u]

                    # Check all vertices connected to u
                    for neighbor in graph[u]:
                        # if neighbor is not visited yet -> simply color the opposite color for neighbor
                        if visited[neighbor] == 0:
                            visited[neighbor] = -uColor
                            queue.append(neighbor)
                        else:
                            neighborColor = visited[neighbor]
                            if uColor == neighborColor:
                                return False

        return True


    # --------------------------------------------------------------------
    # Leetcode 909. Snakes and Ladders
    def printGraph(self, graph: List[List[int]]):
        for i, edges in enumerate(graph):
            neighbors = ', '.join(str(v) for v in edges)
            print(f"Node {i}: [{neighbors}]")

    def graphRepresentation(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        graph = [[] for _ in range(n * n)]
        # ----------------------
        def get_coordinates(square: int) -> Tuple[int, int]:
            # Convert 1-based square number to (row, col)
            row = n - 1 - (square - 1) // n
            col = (square - 1) % n
            if (n - row) % 2 == 0:
                col = n - 1 - col
            return row, col
        # ----------------------
        for i in range(1, n * n + 1):
            for move in range(1, 7):
                next_square = i + move
                if next_square > n * n:
                    continue
                r, c = get_coordinates(next_square)
                dest = board[r][c] if board[r][c] != -1 else next_square
                graph[i - 1].append(dest - 1)

        return graph

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        graph = self.graphRepresentation(board)
        self.printGraph(graph)

        # Start BFS
        visited = [False for _ in range (len(graph))]
        path = [-1 for _ in range (len(graph))]
        dq = deque([0])
        visited[0] = True

        while dq:
            pop = dq.popleft()
            for neighbor in graph[pop]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    path[neighbor] = pop
                    dq.append(neighbor)
        
        # Trace path
        print("path: ", path)
        steps = 1
        current = path[-1]
        while current != 0:
            steps += 1
            # Impossible to reach the end
            if current == path[current]:
                return -1
            current = path[current]

        return steps
    
    # --------------------------------------------------------------------
    # Leetcode 1091. Shortest Path in Binary Matrix
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        visited = set()
        dq = deque()
        dq.append( ((0, 0), 0) )            # (node, distance from top-left cell to node)
        visited.add((0,0))
        # up, upright, right, rightdown, down, downleft, left, leftup
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]         

        # Start of BFS
        while dq:
            node, dist = dq.popleft()
            row, col = node

            # Optimization
            if row == n-1 and col == n-1:
                return dist
            
            # Check each neighbor
            for deltaR, deltaC in directions:
                nr, nc = row + deltaR, col + deltaC
                # Only check if that cell is 0
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dq.append( ((nr, nc), dist+1) )
        
        return -1

    # -------------------------------------------------------------------------------------
    # Leetcode 399. Evaluate Division
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)       # vertice -> [[vertice, multiply weight], ...]
        
        # Populate the undirected graph
        for index, equation in enumerate(equations):
            # u/v = value  -->  u = value * v and v = u * (1/value)
            u, v = equation         
            value = values[index]
            graph[u].append([v, value])
            graph[v].append([u, 1/value])

        # Now, we do BFS for each pair of queries
        # ------------------------------
        def bfs(source, target) -> float:
            visited = set()            
            dq = collections.deque()
            dq.append((source, 1))

            while dq:
                popNode, popWeight = dq.popleft()
                for neighbor, neighborWeight in graph[popNode]:
                    if neighbor not in visited:
                        if neighbor == target:
                            return popWeight * neighborWeight
                        
                        visited.add(neighbor)
                        dq.append((neighbor, popWeight * neighborWeight))

            return -1.0
        # ------------------------------
        results = []
        for u, v in queries:
            results.append(bfs(u, v))

        # print(results)
        return results


    # -------------------------------------------------------------------------------------
    # Leetcode 1730. Shortest Path to Get Food - Premium
    def getFood(self, grid: List[List[str]]) -> int:
        dq = deque()
        visited = defaultdict(int)
        rowLen = len(grid)
        colLen = len(grid[0])

        # Each state will have these info: (row, col, number of step to reach this cell)
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == '*':
                    dq.append((r,c,0))
                    visited[(r,c)] = 0

        # Run BFS
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while dq: 
            popR, popC, popDist = dq.popleft()
            
            # Check if we got food
            if grid[popR][popC] == '#':
                return popDist
            
            # Check each neighbor
            for deltaR, deltaC in directions:
                nR, nC = popR + deltaR, popC + deltaC

                # Make sure neighbor is not oob and it's not an obs
                if 0 <= nR < rowLen and 0 <= nC < colLen and grid[nR][nC] != 'X':
                    if (nR, nC) not in visited or visited[(nR, nC)] > popDist+1:
                        dq.append((nR, nC, popDist+1))
                        visited[(nR, nC)] = popDist + 1
        
        return -1

        




    """ Multi-source BFS """
    # --------------------------------------------------------------------
    # Leetcode 542. 01 Matrix
    #   Solution 1: Brute-force BFS from each "1" cell
    # Time complexity: O((m.n)^2)
    # --> Worst case scenario: all cells are "1" except for the last cell
    #   Solution 2: Multi-source BFS - all "0" cells are treated as starting points
    # Time complexity: O(m.n) where each cell is only visited once
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rowLen = len(mat)
        colLen = len(mat[0])

        # BFS
        result = [[-1 for _ in range(colLen)] for _ in range(rowLen)]
        dq = deque()

        # Populate queue with all "0" cells
        for r in range(rowLen):
            for c in range(colLen):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    dq.append((r,c))

        # Multi-source BFS
        while dq:
            popR, popC = dq.popleft()
            # Check each neighbor
            for deltaR, deltaC in directions:
                nR, nC = popR + deltaR, popC + deltaC
                # 'result' can act as 'visited' set in this case, making sure each cell is only visited once
                # if result[nR][nC] == -1, mat[nR][nC] is "1" for sure
                if 0 <= nR < rowLen and 0 <= nC < colLen and result[nR][nC] == -1:
                    result[nR][nC] = result[popR][popC] + 1
                    dq.append((nR, nC))

        return result

    # --------------------------------------------------------------------
    # Leetcode 1162. As Far from Land as Possible
    def maxDistance(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])

        # Treat all land cells as starting point
        # distance cell will be initialized as -1 for land cells, and 0 for water cells
        dq = deque([])
        distances = [[-1 for _ in range(colLen)] for _ in range(rowLen)]        # act as 'visited'
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 0:
                    distances[r][c] = 0
                else:
                    dq.append((r,c))

        # Multi-source BFS
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        step = 0
        maxDist = -1
        while dq: 
            step += 1

            # Process all cells on the same layer
            for _ in range(len(dq)):
                popRow, popCol = dq.popleft()
                
                # Check each neighbor
                for deltaRow, deltaCol in directions:
                    nR, nC = popRow + deltaRow, popCol + deltaCol
                    # Make sure neighbor is not oob and not visited yet
                    if 0 <= nR < rowLen and 0 <= nC < colLen and distances[nR][nC] == 0:
                        distances[nR][nC] = step
                        maxDist = max(maxDist, step)
                        dq.append((nR, nC))

        return maxDist
      

    # --------------------------------------------------------------------
    # Leetcode 994. Rotting Oranges 
    def orangesRotting(self, grid: List[List[int]]) -> int:      
        rotten = set()      # equivalence of 'visited'
        dq = deque()
        timeAffected = 0
        freshOrange = 0

        # Step 1: Initialize queue and count fresh oranges
        # Each rotten orange is a source
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c] == 1:
                    freshOrange += 1
                elif grid[r][c] == 2:
                    dq.append((r,c))
                    rotten.add((r,c))

        # ---------------------------------------
        def bfs(): 
            nonlocal timeAffected, freshOrange

            # freshOrange > 0 is important, as this avoids over-count the last layer
            while dq and freshOrange > 0:
                timeAffected += 1

                # Each minute passes, we need to process the whole layer instead of just one cell
                for _ in range (len(dq)):
                    rPop, cPop = dq.popleft()
                    directions = [(rPop-1,cPop), (rPop,cPop+1), (rPop+1,cPop), (rPop,cPop-1)] # up, right, down, left

                    for direction in directions:
                        r, c = direction
                        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1 and (r,c) not in rotten:
                            rotten.add((r,c))
                            dq.append((r,c))
                            freshOrange -= 1
        # ---------------------------------------

        # Step 2: BFS to simulate rotting process
        bfs()        

        return timeAffected if freshOrange == 0 else -1

    # --------------------------------------------------------------------
    # Leetcode 286. Walls and Gates
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # visited = set()
        dq = deque()
        steps = 0

        # Initialize the queue with all the gates
        for r in range (len(rooms)):
            for c in range (len(rooms[0])):
                if rooms[r][c] == 0:
                    # visited.add((r,c))
                    dq.append((r,c))

        # Run BFS algo
        while dq:
            steps += 1

            # All cells on the same layer should be processed at the same time
            for _ in range (len(dq)):
                rPop, cPop = dq.popleft()
                
                # Check all neighbors
                directions = [(rPop-1,cPop), (rPop,cPop+1), (rPop+1,cPop), (rPop,cPop-1)]   # up, right, down, left
                for direction in directions:
                    r, c = direction
                    if 0 <= r < len(rooms) and 0 <= c < len(rooms[0]) and rooms[r][c] not in (-1,0):
                        if steps < rooms[r][c]:
                            rooms[r][c] = steps
                            dq.append((r,c))

        print(rooms)







    """ Hard """
    # ====================================================================
    # Leetcode 847. Shortest Path Visiting All Nodes
    # This problem follows State BFS -> the most generalized form of BFS
    # One node can have multiple stages. If graph has 12 nodes, and each node can either be visited or not --> 2^12 states
    # 12 original nodes * 2^12 => 12 * 2^12 states for a generalized graph
    # We can no longer just represent a node with its value. It has to be
    # node = (i, (true/false * n)) -> i is the value of the current node
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        visited = set()
        shortestPath = 0
        dq = deque()
        
        # Initialize queue
        for nodeValue in range(len(graph)):
            nodeStage = (nodeValue, [False for _ in range(len(graph))])     # node = (i, (true/false * n)) -> i is the value of the current node
            nodeStage[1][nodeValue] = True      # second item of tuple nodeStage is a List, so it's mutable
            dq.append(nodeStage)    
            visited.add((nodeStage[0], tuple(nodeStage[1])))    # cannot add mutable data type into a set()
            
        # Run general BFS
        while True:
            # Process each layer
            for _ in range(len(dq)):    
                pop = dq.popleft()
                nodeValue = pop[0]
                stages = pop[1]
                stop = True
                for stage in stages:
                    # If all stage are True, stop BFS
                    stop = stop and stage
                    
                # Condition to stop our BFS 
                if stop: 
                    return shortestPath 
                    
                # Check each neighbor of pop
                for neighbor in graph[nodeValue]:
                    newStage = stages.copy()
                    newStage[neighbor] = True
                    if (neighbor, tuple(newStage)) not in visited:
                        dq.append((neighbor, newStage))
                        visited.add((neighbor, tuple(newStage)))
                    
            # Increment the distance for each layer
            shortestPath += 1
        
    # --------------------------------------------------------------------
    # Leetcode 1293. Shortest Path in a Grid with Obstacles Elimination
    # Another Generalized state BFS
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = defaultdict(int)
        dq = deque([(0, 0, k, 0)])                              # (row, col, number of obs elimination left, distance from 'start')
        visited[(0,0)] = k
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]         # up, right, down, left

        # Run generalized BFS
        while dq:
            popRow, popCol, popK, popDist = dq.popleft()

            # Check if we reach the end
            # Optimization: 
            # BFS explores all paths in increasing order of distance
            # The first time you reach the target cell (m-1, n-1), it’s guaranteed to be via the shortest possible path
            # Any later visit to the same cell will be equal or longer, so you don’t need to track min()
            if popRow == (len(grid)-1) and popCol == (len(grid[0])-1):
                return popDist

            # Check each neighbor
            for deltaR, deltaC in directions:
                nR, nC = popRow + deltaR, popCol + deltaC
                
                # First, make sure nR and nC is not oob
                if 0 <= nR < len(grid) and 0 <= nC < len(grid[0]):
                    # Optimization: prune worse paths
                    # Also skip if we have been to neighbor cell with more or equal k remaining eliminations
                    # Case 1: if neighbor is empty and not visited yet
                    if grid[nR][nC] == 0 and ((nR, nC) not in visited or visited[(nR, nC)] < popK):
                        dq.append((nR, nC, popK, popDist+1))
                        visited[(nR, nC)] = popK
                    # Case 2: if neighbor is an obs and popK > 0
                    elif grid[nR][nC] == 1 and popK > 0 and ((nR, nC) not in visited or visited[(nR, nC)] < popK-1):
                        dq.append((nR, nC, popK-1, popDist+1))
                        visited[(nR, nC)] = popK-1

        return -1
        

    # --------------------------------------------------------------------
    # Leetcode 127. Word Ladder
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = {}
        path = {}

        # Edge case: endWord is not in the wordList
        # Also prepare the 'visited' and 'path' array
        beginWordInList = False
        endWordInList = False
        for word in wordList:
            visited[word] = False
            path[word] = None
            if word == endWord:
                endWordInList = True
            if word == beginWord:
                beginWordInList = True
        
        if not endWordInList: return 0
        if not beginWordInList: 
            wordList.append(beginWord)
            visited[beginWord] = False
            path[beginWord] = None
        
        # Step 1: Construct a graph representation - O(n*m) for n is # word inwordList and m is len(word)
        # This graph will be constructed using each pattern of a word. All words share the same pattern are connected by a bi-directional edge
        # Ex: '*ot': ['hot', 'dot', 'lot']
        graph = defaultdict(list)

        # 'word' all have the same len
        for word in wordList:
            for i in range (len(word)):
                pattern = word[:i] + "*" + word[i+1:]       # eg. h*t
                graph[pattern].append(word)

        # print("graph: ", graph)
        # print("wordList: ", wordList)

        # Step 2: Run BFS
        dq = deque([beginWord])
        visited[beginWord] = True

        while dq:
            pop = dq.popleft()

            # Check all neighbor of pop
            for i in range (len(pop)):
                pattern = pop[:i] + "*" + pop[i+1:]       # eg. h*t
                # All words in graph[pattern] will be the neighbor of pop
                for neighbor in graph[pattern]:
                    if neighbor != pop:
                        if neighbor in visited and visited[neighbor] == False:
                            visited[neighbor] = True
                            path[neighbor] = pop
                            dq.append(neighbor)
            
        # print("path: ", path)
        # print("visited: ", visited)

        # Step 3: Trace path
        count = 1
        word = endWord
        while word != beginWord:
            count += 1
            word = path[word]
            # At any point, if we couldn't reach the next word, it means no is no sequence to go from beginWord->endWord
            if word == None: 
                return 0

        return count
    
    # --------------------------------------------------------------------
    # Leetcode 126. Word Ladder II
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Edge case: endWord is not in the wordList
        # Also prepare the 'visited' and 'path' array
        beginWordInList = False
        endWordInList = False
        for word in wordList:
            if word == endWord:
                endWordInList = True
            if word == beginWord:
                beginWordInList = True
        
        if not endWordInList: return []
        if not beginWordInList: 
            wordList.append(beginWord)
        
        # Step 1: Construct a graph representation - O(n*m) for n is # word inwordList and m is len(word)
        # This graph will be constructed using each pattern of a word. All words share the same pattern are connected by a bi-directional edge
        # Ex: '*ot': ['hot', 'dot', 'lot']
        graph = defaultdict(list)

        # 'word' all have the same len
        for word in wordList:
            for i in range (len(word)):
                pattern = word[:i] + "*" + word[i+1:]       # eg. h*t
                graph[pattern].append(word)

        # print("graph: ", graph)
        # print("wordList: ", wordList)

        # Step 2: Run BFS
        dq = deque([beginWord])
        parents = defaultdict(list)       # equivalent of 'path'
        distance = {beginWord: 0}         # equivalent of 'visited', recording the distance between 'word' and 'beginWord'

        while dq:
            pop = dq.popleft()

            # Check all neighbor of pop
            for i in range (len(pop)):
                pattern = pop[:i] + "*" + pop[i+1:]       # eg. h*t
                # All words in graph[pattern] will be the neighbor of pop
                for neighbor in graph[pattern]:
                    # Case 1: if 'neighbor' is not visited yet
                    if neighbor not in distance:
                        distance[neighbor] = distance[pop] + 1
                        parents[neighbor].append(pop)
                        dq.append(neighbor)
                    # Case 2: if distance beginWord->neighbor is the same as distance[pop] + 1, then going from pop-> neighbor is another path
                    elif distance[neighbor] == distance[pop] + 1:
                        parents[neighbor].append(pop)
            
        # print("parents: ", parents)
        # print("distance: ", distance)

        # Step 3: Trace path using DFS
        # -------------------------------------
        def dfs(word: str, path: List[str]):
            # Base case
            if word == beginWord:
                result.append(path[::-1])
            # dfs
            for parent in parents[word]:
                dfs(parent, path + [parent])
        # -------------------------------------

        result = []
        if endWord in parents:
            dfs(endWord, [endWord])

        # print(result)
        return result

    # --------------------------------------------------------------------
    # Leetcode 864. Shortest Path to Get All Keys
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        dq = deque([])
        startingRow = -1
        startingCol = -1
        totalKey = 0
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c].isalpha():
                    totalKey += 1
                elif grid[r][c] == '@':
                    startingRow = r
                    startingCol = c

        # Perform generalized BFS
        totalKey //= 2
        # Each state will contains these info: row, col, and a bool tuple of len 'totalKey', each value representing if that 
        # particular key has been collected
        dq.append((startingRow, startingCol, tuple([False for _ in range(totalKey)])))
        visited = set()
        visited.add((startingRow, startingCol, tuple([False for _ in range(totalKey)])))               # Each node will be a state
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        step = 0

        while dq: 
            step += 1

            # Process all cells on the same layer
            for _ in range(len(dq)):
                popR, popC, popKeyStates = dq.popleft()

                # Check each neighbor
                for deltaRow, deltaCol in directions:
                    nR, nC = popR + deltaRow, popC + deltaCol

                    # Make sure neighbor is not oob and neighbor is not a wall:
                    if 0 <= nR < rowLen and 0 <= nC < colLen and grid[nR][nC] != '#':
                        # Case 0: If neighbor is an empty space
                        if grid[nR][nC] == '.' or grid[nR][nC] == '@':
                            # Check if we have visited the next state, not just the next cell
                            if (nR, nC, popKeyStates) not in visited:
                                visited.add((nR, nC, popKeyStates))
                                dq.append((nR, nC, popKeyStates))
                        # Case 1: If neighbor is a lock
                        elif grid[nR][nC].isalpha() and 65 <= ord(grid[nR][nC]) <= 70:
                            # Check if we have already collected the key for this lock and the next state is not visited yet -> move into that cell
                            if popKeyStates[ord(grid[nR][nC]) - 65] == True and (nR, nC, popKeyStates) not in visited:
                                visited.add((nR, nC, popKeyStates))
                                dq.append((nR, nC, popKeyStates))
                        # Case 2: If neighbor is a key
                        else:
                            keyIndex = ord(grid[nR][nC]) - 97
                            popKeyStatesList = list(popKeyStates)
                            popKeyStatesList[keyIndex] = True
                            popKeyStatesTuple = tuple(popKeyStatesList)

                            # Check if we reach finishing state
                            allKeyCollected = True
                            for keyCollected in popKeyStatesTuple:
                                # If one key is not collected yet, still more work to do
                                if not keyCollected:
                                    allKeyCollected = False 
                                    break
                            
                            if allKeyCollected:
                                return step
                
                            if (nR, nC, popKeyStatesTuple) not in visited:
                                visited.add((nR, nC, popKeyStatesTuple))
                                dq.append((nR, nC, popKeyStatesTuple))

        return -1


























if __name__ == "__main__":
    leetcode = Solution()

    # ---------------------------------
    # n = 3
    # red_edges = [[0,1]]
    # blue_edges = [[1,2]]

    # distance = leetcode.shortestAlternatingPaths(n, red_edges, blue_edges)
    # print(distance)

    # -------------------------------------------
    # deadends = ["0201","0101","0102","1212","2002"] 
    # target = "0202"

    # min_turns = leetcode.openLock(deadends, target)
    # print(min_turns)

    # -------------------------------------------
    # graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    # print(leetcode.isBipartite(graph))

    # --------------------------- 994 ---------------------------
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    # answer994 = leetcode.orangesRotting(grid)
    # print("answer994: ", answer994)

    # --------------------------- 286 ---------------------------
    # rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    # leetcode.wallsAndGates(rooms)

    # --------------------------- 909 ---------------------------
    # board = [[1,1,-1],[1,1,1],[-1,1,1]]
    # # board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    # print(leetcode.snakesAndLadders(board))

    # --------------------------- 1730 ---------------------------
    grid = [["X","X","X","X","X"],
            ["X","*","X","O","X"],
            ["X","O","X","#","X"],
            ["X","X","X","X","X"]]
    leetcode.getFood(grid)


    # --------------------------- 127 + 126 ---------------------------
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log","cog"]
    # leetcode.findLadders(beginWord, endWord, wordList)

    # --------------------------- 1091 ---------------------------
    # grid = [[0,0,0],[1,1,0],[1,1,0]]
    # leetcode.shortestPathBinaryMatrix(grid)

    # --------------------------- 847 ---------------------------
    # graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    # print(leetcode.shortestPathLength(graph))

    # --------------------------- 864 ---------------------------
    # grid = ["@.a..","###.#","b.A.B"]
    # print(leetcode.shortestPathAllKeys(grid))    

    # --------------------------- 542 ---------------------------
    # mat = [[0,0,0],[0,1,0],[1,1,1]]
    # print(leetcode.updateMatrix(mat))