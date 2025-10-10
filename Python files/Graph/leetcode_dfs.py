"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Depth First Search =========================================================
Leetcode 17. Letter Combinations of a Phone Number
Leetcode 841. Keys and Rooms
Leetcode 200. Number of Islands 
Leetcode 529. Minesweeper
Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero (Hard version: Leetcode 2858)
Leetcode 133. Clone Graph
Leetcode 1245. Tree Diameter
Leetcode 490. The Maze

"""
 
from typing import List
import bisect

# For LC 133. Clone graph
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    # Leetcode 17. Letter Combinations of a Phone Number  
    def letterCombinations(self, digits: str) -> List[str]:
        # create a data strucutre to store answers
        ans = []

        if digits != None and len(digits) > 0:
            mapping = ["", "", "abc", "def", "ghi", "jkl","mno","pqrs","tuv","wxyz"]
            d = digits[0] # if digits == "23" then d == "2"
            letters = mapping[ int(d) ] # letters == "abc"
            for char in letters:     
                self.dfs(digits, mapping, ans, 1, char)
            
        return ans

    def dfs(self, digits: str, mapping: List[str], ans: List[str], index: int, potential: str):
        # base cases: we found 1 combination
        if len(potential) == len(digits):
            ans.append(potential)
            return 
            
        # variation
        d = digits[index] # d == 2
        letters = mapping[ int(d) ]
        for char in letters:
            self.dfs(digits, mapping, ans, index + 1, potential + char)


    # -------------------------------------------------------------------------------------
    # Leetcode 841. Keys and Rooms
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # initialization
        visited = [ False for _ in range(len(rooms)) ]

        # dfs
        s = [0]
        visited[0] = True 
        cnt = 1

        while len(s):
            u = s.pop()
            for v in rooms[u]:
                if not visited[v]:
                    visited[v] = True
                    cnt += 1
                    s.append(v)

        return cnt == len(rooms)

    # -------------------------------------------------------------------------------------
    # Leetcode 200. Number of Islands
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                if grid[i][j] == "1":
                    ans += self.bfs(grid, i, j)
        
        return ans
    

    def bfs(self, grid: List[List[str]], i: int, j: int) -> int:
        # corner cases
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return 0

        # most important line
        grid[i][j] = "0"
        # check all 4 adjacents and turn them into 0 if 1 is found
        self.bfs(grid, i-1, j) # up
        self.bfs(grid, i+1, j) # down
        self.bfs(grid, i, j-1) # left
        self.bfs(grid, i, j+1) # right

        # finally, return that you found 1 island
        return 1

        
    # -------------------------------------------------------------------------------------
    # Leetcode 529. Minesweeper
    def adjacentMines(self, board: List[List[str]], click: List[int]) -> int:
        i, j = click
        
        num_mines = 0
        for r in range (i-1, i+2):
            for c in range (j-1, j+2):
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                    if board[r][c] == "M":
                        num_mines += 1

        return num_mines
                    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        If click on "M" 
            -> game over
        else if click on "E"
            if no adjacent mines
                reveal it as "B"
            else
                digit 1->8
        """
        i, j = click
        
        # 1. If a mine ('M') is revealed, then the game is over - change it to 'X'
        if board[i][j] == 'M': 
            board[i][j] = 'X'
        # 2. If an empty square ('E') is revealed
        else: 
            # compute number of adjacent mines
            num_mines = self.adjacentMines(board, click)
            if num_mines: 
                board[i][j] = str(num_mines)
            else: 
                board[i][j] = "B"
                for r in range (i-1, i+2):
                    for c in range (j-1, j+2):
                        if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] != "B":
                            self.updateBoard(board, [r, c])
                
        return board



    # -------------------------------------------------------------------------------------
    # Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero
    # Treat the graph as directed. Start a dfs from the root, if you come across an edge 
    # in the forward direction, you need to reverse the edge.
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Set up graph
        graph = [set() for _ in range(n)] # list of set to reduce look up time
        neighbor = [[] for _ in range(n)]
        # can you reach 0 from city i-th
        reachable_0 = [False for _ in range(n)]
        reachable_0[0] = True
        for con in connections:
            u, v = con
            graph[u].add(v)
            neighbor[u].append(v)
            neighbor[v].append(u)

        # run dfs
        change = 0
        stack = []
        stack.append(0)
        while stack: 
            u = stack.pop()
            for v in neighbor[u]:
                if not reachable_0[v]:
                    # after this, v can reach 0
                    reachable_0[v] = True
                    stack.append(v)                   
                    # check if all cities that v points to can reach to 0
                    if (0 not in graph[v]) and (u not in graph[v]):
                        change += 1

        return change


    # -------------------------------------------------------------------------------------
    # Leetcode 133. Clone Graph
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None  # Edge case: empty graph

        # Dictionary to map original nodes to their cloned counterparts
        cloned = {}

        def dfs(current: 'Node') -> 'Node':
            # If the node is already cloned, return the clone
            if current in cloned:
                return cloned[current]

            # Step 1: Clone the current node (without neighbors for now)
            copy = Node(current.val)
            cloned[current] = copy  # Mark this node as cloned

            # Step 2: Recursively clone all neighbors
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        # Start DFS from the given node
        return dfs(node)


    # -------------------------------------------------------------------------------------
    # Leetcode 1245. Tree Diameter
    # DFS from root to find the furthest node (x1)
    # DFS from x1 to find the furthest node x2
    # Diameter of the tree will be |x2-x1|
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        # Graph representation
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 1: DFS from a random node to find the furthest node (x1)
        stack = [(0,0)]     # (node, distance from root)
        visited = [False for _ in range(n)]
        visited[0] = True
        furthestDistance = 0
        furthestNode = None

        while stack:
            popNode, popDist = stack.pop()
            for neighbor in graph[popNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, popDist+1))
                    if popDist+1 > furthestDistance:
                        furthestDistance = popDist+1
                        furthestNode = neighbor

        # Step 2: DFS from furthestNode
        stack = [(furthestNode,0)]     # (node, distance from root)
        visited = [False for _ in range(n)]
        visited[furthestNode] = True
        furthestDistance = 0
        # furthestNode2 = None

        while stack:
            popNode, popDist = stack.pop()
            for neighbor in graph[popNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, popDist+1))
                    if popDist+1 > furthestDistance:
                        furthestDistance = popDist+1
                        # furthestNode2 = neighbor

        return furthestDistance


    # -------------------------------------------------------------------------------------
    # Leetcode 490. The Maze
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rowLen = len(maze)
        colLen = len(maze[0])
        wallsIdxForEachRow = [[] for _ in range(rowLen)]
        wallsIdxForEachCol = [[] for _ in range(colLen)]
        for r in range(rowLen):
            for c in range(colLen):
                if maze[r][c] == 1:
                    wallsIdxForEachRow[r].append(c)
                    wallsIdxForEachCol[c].append(r)

        # print(wallsIdxForEachCol)
        # print(wallsIdxForEachRow)

        stack = [(start[0], start[1])]
        visited = set()
        visited.add( (start[0], start[1]) )

        while stack:
            pr, pc = stack.pop()
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

            for nextR, nextC in [(upR, upC), (rightR, rightC), (downR, downC), (leftR, leftC)]:
                if (nextR, nextC) not in visited:
                    if nextR == destination[0] and nextC == destination[1]:
                        return True
                    stack.append((nextR, nextC))
                    visited.add((nextR, nextC))

        return False


    # Leetcode 505. The Maze II
    # For LC490 we can use DFS with 'visited' set because we only have to check if it's possible to reach the destination.
    # However, for this LC 505, DFS with 'visited' set can potentially skip shorter paths if a longer one already reached a node first.
    # We cannot use BFS either because each edge has a different weight. BFS would work if we want the path with the minimum hops (each hop has weight of 1)
    # For this problem, we need to use Dijkstra. Find the solution in "Python files\Graph - Shortest path in graph\dijkstra.py"
    # -------------------------------------------------------------------------------------





















if __name__=="__main__":
    leetcode = Solution()
    
    # -------------- 841 --------------
    #rooms = [ [1], [2], [3], [] ]
    #access = leetcode.canVisitAllRooms(rooms)
    #print(access)

    # -------------- 200 --------------
    # grid =[ ["1","1","0","0","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","1","0","0"],
    #         ["0","0","0","1","1"] ]
    
    # numIs = leetcode.numIslands(grid)
    # print(numIs)
    
    # --------------- 207 ---------------
    # numCourses = 20
    # prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    # print(leetcode.canFinish(numCourses, prerequisites))

    # --------------- 490 + 505 ---------------
    maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
    start = [0,0]
    destination = [8,6]
    # ans490 = leetcode.hasPath(maze, start, destination)
    # print(ans490)





