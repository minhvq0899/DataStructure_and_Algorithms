"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Depth First Search =========================================================
1. Leetcode 17. Letter Combinations of a Phone Number
2. Leetcode 841. Keys and Rooms
3. Leetcode 200. Number of Islands 
4. Leetcode 529. Minesweeper

"""
 
from typing import List

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






