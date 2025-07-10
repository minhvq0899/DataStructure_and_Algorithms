"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Depth First Search =========================================================
1. Leetcode 17. Letter Combinations of a Phone Number
2. Leetcode 841. Keys and Rooms
3. Leetcode 200. Number of Islands 
4. Leetcode 529. Minesweeper
5. Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero (Hard version: Leetcode 2858)
6. Leetcode 133. Clone Graph

"""
 
from typing import List

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
    numCourses = 20
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    print(leetcode.canFinish(numCourses, prerequisites))


    # --------------- 210 ---------------






