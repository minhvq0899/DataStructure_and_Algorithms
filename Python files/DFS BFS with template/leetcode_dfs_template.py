"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= DFS with template =========================================================
DFS down different path: 
    1. Leetcode 22. Generate Parentheses
    2. Leetcode 17. Letter Combinations of a Phone Number
    3. Leetcode 752. Open the Lock
    4. Leetcode 39. Combination Sum

DFS on grid/ matrix
    1. Leetcode 417. Pacific Atlantic Water Flow
    2. Leetcode 1020. Number of Enclaves
    3. Leetcode 529. Minesweeper
    4. Leetcode 695. Max Area of Island
    5. Leetcode 1254. Number of Closed Islands
    6. Leetcode 130. Surrounded Regions
    7. Leetcode 1306. Jump Game III
    8. Leetcode 934. Shortest Bridge ??
"""

import queue
from typing import List
import collections

class Solution:
    # Leetcode 22. Generate Parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        
        self.dfs_paren(n, "", 0, 0, combinations)

        return combinations

    def dfs_paren(self, n: int, potential: str, left: int, right: int, combinations: List[str]):
        # base case
        if len(potential) == 2*n:
            combinations.append( potential )
            return
        
        # variation
        if left < n:
            self.dfs_paren(n, potential + "(", left+1, right, combinations)
        if right < left:
            self.dfs_paren(n, potential + ")", left, right+1, combinations)
        
    
    # -----------------------------------------------------------------------------------------------
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


    # ------------------------------------------------------------------------------------------
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
    
    def openLock_2025(self, deadends: List[str], target: str) -> int:
        if target == "0000": return 0
        deadend_set = set(deadends)
        if "0000" in deadend_set: return -1

        # paths will act as both Visited set and Path dict
        paths = collections.defaultdict(str)
        paths["0000"] = None
        q = queue.Queue()
        q.put("0000")

        while not q.empty():
            u = q.get()
            if u not in deadend_set:
                neighbors = self.find_neighbor(u)
                for neighbor in neighbors:
                    if neighbor not in paths and neighbor not in deadend_set:
                        paths[neighbor] = u
                        q.put(neighbor)
        
        for key,value in paths.items():
            print ("{}: {} \n".format(key,value) )

        answer = 0
        if target in paths:
            while target != "0000":
                target = paths[target]
                answer += 1
            return answer

        return -1



    # ------------------------------------------------------------------------------------------
    # Leetcode 39. Combination Sum
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # ------------------------------------------------------------------------------
        def subsetCount(tar, potential, curIdx):
            # base case 1: found a combination
            if tar == 0: 
                ans.append(list(potential))
                return
            # base case 2: index out of bound
            if curIdx not in range (len(candidates)):
                return 
            # base case 3: target < 0
            if tar < 0:
                return 

            # recursive part
            # use that current index
            subsetCount(tar-candidates[curIdx], potential + [candidates[curIdx]], curIdx)
            # potential.pop()     # other solution will use this to backtrack
            # not use that current index <------ but we already backtrack with this
            subsetCount(tar, potential, curIdx + 1)
            
        # ------------------------------------------------------------------------------
        poten = list()
        subsetCount(target, poten, 0)
        return ans

    def combinationSum_leetcode_solution(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # ------------------------------------------------------------------------------
        def subsetCount(tar, potential, start):
            # base case 1: found a combination
            if tar == 0: 
                ans.append(list(potential))
                return
            # base case 2: target < 0
            if tar < 0:
                return 

            for i in range (start, len(candidates)):
                potential.append(candidates[i])
                # recursive call
                subsetCount(tar-candidates[i], potential, i)
                # back track
                potential.pop()
        # ------------------------------------------------------------------------------
        subsetCount(target, [])
        return ans

  





    # ================================================================================================================================================================================================================================================================================== 
    # ================================================================================================================================================================================================================================================================================== 
 
 


 
 
 
 
    # Leetcode 417. Pacific Atlantic Water Flow
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        DFS for this problem takes: matrix, coordinate, previous value, ocean grid
        We don't have to send ans = [] along to record changes. All changes will be recorded in ocean parameter
        """

        # matrix is empty
        if not matrix: return []
        
        m = len(matrix)
        n = len(matrix[0])
        # create 2 Boolean matrixs for Pacific and Atlantic
        pacific = [[False for _ in range (n)] for _ in range (m)]
        atlantic = [[False for _ in range (n)] for _ in range (m)]

        # create a data structure to store answers
        # doesn't have to for this problem

        # Top-Pacific and Bottom-Atlantic
        for i in range(n):
            self.dfs_pacificAtlantic(matrix, [0, i], float('-inf'), pacific)
            self.dfs_pacificAtlantic(matrix, [m-1, i], float('-inf'), atlantic)
            
        # Left-Pacific and Right-Atlantic
        for i in range(m):
            self.dfs_pacificAtlantic(matrix, [i, 0], float('-inf'), pacific)
            self.dfs_pacificAtlantic(matrix, [i, n-1], float('-inf'), atlantic)

        # count satisfied coordinates
        ans = []
        for r in range (m):
            for c in range (n):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r, c])
        
        return ans


    def dfs_pacificAtlantic(self, matrix: List[List[int]], coordinate: List[List[int]], prev: float, ocean: List[List[bool]]):
        r, c = coordinate
        m = len(matrix)
        n = len(matrix[0])
        # 3 base cases
        if r < 0 or c < 0 or r >= m or c >= n:
            return 
        if prev > matrix[r][c]:
            return  
        if ocean[r][c]: 
            return

        # TO DO
        ocean[r][c] = True

        # Call BFS as needed    
        top = [r-1, c]
        down = [r+1, c]
        left = [r, c-1]
        right = [r, c+1]

        self.dfs_pacificAtlantic(matrix, top, matrix[r][c], ocean)
        self.dfs_pacificAtlantic(matrix, down, matrix[r][c], ocean)
        self.dfs_pacificAtlantic(matrix, left, matrix[r][c], ocean)
        self.dfs_pacificAtlantic(matrix, right, matrix[r][c], ocean)


    # --------------------------------------------------------------------------------------
    # Leetcode 1020. Number of Enclaves
    def numEnclaves(self, A: List[List[int]]) -> int:
        count = 0

        # initialize DFS
        # first, initialize DFS for all boundary grids
        for m in range (len(A)): 
            if A[m][0] == 1: # left
                self.dfs_numEnclaves(A, m, 0)
            if A[m][len(A[0])-1] == 1: # right
                self.dfs_numEnclaves(A, m, len(A[0])-1)
        
        for n in range (len(A[0])):
            if A[0][n] == 1: # top
                self.dfs_numEnclaves(A, 0, n)
            if A[len(A)-1][n] == 1: # bottom
                self.dfs_numEnclaves(A, len(A)-1, n)

        # now, run dfs on all grids that do not touch boundary
        for r in range (1, len(A)-1):
            for c in range (1, len(A[0])-1):
                if A[r][c] == 1:
                    count += 1

        return count

    def dfs_numEnclaves(self, A: List[List[int]], r: int, c: int):
        # base cases
        if r < 0 or c < 0 or r >= len(A) or c >= len(A[0]):
            return 
        if A[r][c] == 0:
            return 

        # TO DO
        A[r][c] = 0

        # call DFS where needed
        self.dfs_numEnclaves(A, r-1, c) # top
        self.dfs_numEnclaves(A, r+1, c) # down
        self.dfs_numEnclaves(A, r, c-1) # left
        self.dfs_numEnclaves(A, r, c+1) # right
        
    # Time: O(m*n)?
    # Space: O(1)


    # --------------------------------------------------------------------------------------
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
    
    """
    Time Complexity: O()
    Extra Space Complexity: O(1)
    """


    # --------------------------------------------------------------------------------------
    # Leetcode 695. Max Area of Island
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        area = 0

        # call DFS on each grid cell
        for r in range ( len(grid) ):
            for c in range ( len(grid[0]) ):
                if grid[r][c] == 1:
                    area =  max(area, self.dfs_maxArea( [r,c], grid ) )

        return area
        """
        Time Complexity: O(row * cow)
        Extra Space Complexity: O(1)
        """

    # Initialize DFS
    def dfs_maxArea(self, coordinate: List[int], grid: List[List[int]]) -> int:
        r, c = coordinate
        # base cases
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 0
        if grid[r][c] == 0:
            return 0
        
        # TO DO
        grid[r][c] = 0
        count = 1
    
        # call DFS where needed
        count += self.dfs_maxArea( [r-1,c], grid ) # top
        count += self.dfs_maxArea( [r+1,c], grid ) # down
        count += self.dfs_maxArea( [r,c-1], grid ) # left
        count += self.dfs_maxArea( [r,c+1], grid ) # right

        return count
        
        
    # --------------------------------------------------------------------------------------
    # Leetcode 1254. Number of Closed Islands
    def closedIsland(self, grid: List[List[int]]) -> int:
        # find all islands that touch boundary (they are not closed islands)
        for r in range (len(grid)): 
            if grid[r][0] == 0:
                self.dfs_closedIsland( [r, 0], grid ) # left
            if grid[r][len(grid[0]) - 1] == 0:
                self.dfs_closedIsland( [r, len(grid[0])-1], grid ) # right

        for c in range (len(grid[0])):
            if grid[0][c] == 0:
                self.dfs_closedIsland( [0, c], grid ) # top
            if grid[len(grid)-1][c] == 0:
                self.dfs_closedIsland( [len(grid)-1, c], grid ) # bottom

        # now all islands left are closed islands
        num_closed = 0
        for r in range (1, len(grid)-1):
            for c in range (1, len(grid[0])-1):
                if grid[r][c] == 0:
                    num_closed += 1
                    self.dfs_closedIsland( [r, c], grid ) 

        return num_closed
        """
        Time Complexity: O(row * col)
        Extra Space Complexity: O(1)
        """

    def dfs_closedIsland(self, coordinate: List[int], grid: List[List[int]]):
        r, c = coordinate
        # Base cases
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 
        if grid[r][c] == 1:
            return 

        # TO DO
        grid[r][c] = 1

        # Call DFS where needed
        self.dfs_closedIsland( [r-1, c], grid ) # top
        self.dfs_closedIsland( [r+1, c], grid ) # down
        self.dfs_closedIsland( [r, c-1], grid ) # left
        self.dfs_closedIsland( [r, c+1], grid ) # right
    

    # --------------------------------------------------------------------------------------
    # Leetcode 130. Surrounded Regions
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 

        m = len(board)
        n = len(board[0])

        # find all the 'O' on boundary and switch them into 'T' (Temporary)
        for r in range (m): 
            if board[r][0] == 'O':
                self.dfs_solve( [r, 0], board ) # left
            if board[r][n - 1] == 'O':
                self.dfs_solve( [r, n-1], board ) # right

        for c in range (n):
            if board[0][c] == 'O':
                self.dfs_solve( [0, c], board ) # top
            if board[m - 1][c] == 'O':
                self.dfs_solve( [m-1, c], board ) # bottom

        # switch all 'O' that don't touch boudary into 'X'
        for r in range (m):
            for c in range (n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
        """
        Time Complexity: O(row * col)
        Extra Space Complexity: O(1)
        """
                    

    def dfs_solve(self, coordinate: List[int], board: List[List[str]]):
        r, c = coordinate
        # Base cases
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return 
        if board[r][c] == 'X' or board[r][c] == 'T':
            return 

        # TO DO
        board[r][c] = 'T'

        # Call DFS where needed
        self.dfs_solve( [r-1, c], board ) # top
        self.dfs_solve( [r+1, c], board ) # down
        self.dfs_solve( [r, c-1], board ) # left
        self.dfs_solve( [r, c+1], board ) # right



    # ------------------------------------------------------------------------
    # Leetcode 1306. Jump Game III
    def canReach(self, arr: List[int], start: int) -> bool:
        reach = []
        
        self.dfs_canReach(arr, start, reach)
        
        return True if reach else False
    
        
    def dfs_canReach(self, arr: List[int], index: int, reach: List[int]):
        # base cases
        if index < 0 or index >= len(arr):
            return 
        if arr[index] == 0:
            reach.append(1)
            return 
        if arr[index] < 0: 
            return 
        
        # TO DO
        arr[index] *= -1
        
        # call DFS where needed
        self.dfs_canReach(arr, index+arr[index], reach)
        self.dfs_canReach(arr, index-arr[index], reach)


    # ------------------------------------------------------------------------------------------


    # # Leetcode 934. Shortest Bridge
    # def shortestBridge(self, A: List[List[int]]) -> int:
    #     pass

    # def dfs_shortestBridge(self, A: List[List[int]], coordinate: List[int], count: int) -> int:
    #     r, c = coordinate

    #     # base cases 
    #     if r < 0 or c < 0 or r >= len(A) or c >= len(A[0]):
    #         return 0
    #     if 


    # --------------------------------------------------------------------------------------------









if __name__ == "__main__":
    leetcode = Solution()

    # ------------------------------------------
    # n = 3
    # expected = ["((()))","(()())","(())()","()(())","()()()"]
    # combinations = leetcode.generateParenthesis(3)
    # print(combinations)
    # assert combinations == expected

    # ------------------------------------------
    # matrix = [[1,2,2,3,5], 
    #           [3,2,3,4,4], 
    #           [2,4,5,3,1], 
    #           [6,7,1,4,5],
    #           [5,1,1,2,4] ]
    # coordinates = leetcode.pacificAtlantic(matrix)

    # print(coordinates)

    # -------------------------------------------
    # A = [ [0,0,0,0],
    #       [1,0,1,0],
    #       [0,1,1,0],
    #       [0,0,0,0] ]
    # ans = leetcode.numEnclaves(A)
    # print(ans)


    # -------------------------------------------
    deadends = ["0201","0101","0102","1212","2002"] 
    target = "0202"

    min_turns = leetcode.openLock_2025(deadends, target)
    print(min_turns)


    # ------------------------ 695: Max Area of Island -------------------------
    # grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    #         [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #         [0,1,1,0,1,0,0,0,0,0,0,0,0],
    #         [0,1,0,0,1,1,0,0,1,0,1,0,0],
    #         [0,1,0,0,1,1,0,0,1,1,1,0,0],
    #         [0,0,0,0,0,0,0,0,0,0,1,0,0],
    #         [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #         [0,0,0,0,0,0,0,1,1,0,0,0,0] ]

    # max_area = leetcode.maxAreaOfIsland(grid)
    # print(max_area)


    # ------------------------- 1254: Number of Closed Islands -------------------------
    # grid = [[1,1,1,1,1,1,1,0],
    #         [1,0,0,0,0,1,1,0],
    #         [1,0,1,0,1,1,1,0],
    #         [1,0,0,0,0,1,0,1],
    #         [1,1,1,1,1,1,1,0] ]
    # num_closed_island = leetcode.closedIsland(grid)
    # print(num_closed_island)


    # ------------------------- 39. Combination Sum -------------------------
    # candidates = [2,3,5]
    # target = 8
    # ans = leetcode.combinationSum(candidates, target)
    # print(ans)

