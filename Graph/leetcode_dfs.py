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

        print(visited)

        return cnt == len(rooms)



    # Leetcode 200. Number of Islands
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                if grid[i][j] == "1":
                    ans += self.bfs(grid, i, j)
                    # print(grid)
        
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
    




    # Leetcode 529. Minesweeper
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i = click[0]
        j = click[1]
        
        # 1. If a mine ('M') is revealed, then the game is over - change it to 'X'
        if board[i][j] == 'M': 
            board[i][j] = 'X'
            return board

        # 2. If an empty square ('E') is revealed
        if board[i][j] == 'E':
            self.bfs_minesweeper(board, click)
            return board

        return board


    # helper bfs
    def bfs_minesweeper(self, board: List[List[str]], click: List[int]):
        i = click[0]
        j = click[1]

        # case exception
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        # case 2 and 3
        try: # top
            top = board[i-1][j]
        except:
            top = "E"

        try: # top_right
            top_right = board[i-1][j+1]
        except:
            top_right = "E"
        
        try: # right
            right = board[i][j+1] 
        except:
            top = "E"
            
        try: # down_right
            down_right = board[i+1][j+1]
        except:
            down_right = "E"
        
        try: # down
            down = board[i+1][j]
        except:
            down = "E"
        
        try: # down_left
            down_left = board[i+1][j-1] 
        except:
            down_left = "E"
        
        try: # left
            left = board[i][j-1]
        except:
            left = "E"
        
        try: # top_left
            top_left = board[i-1][j-1]
        except:
            top_left = "E"
        
                
        # out of bound                    
        if i == 0: # top
            top, top_right, top_left = 'E', 'E', 'E'
        if i == len(board)-1: # bottom
            down, down_right, down_left = 'E', 'E', 'E'
        if j == 0: # left
            left, top_left, down_left = 'E', 'E', 'E'
        if j == len(board[0]) - 1: # right
            right, top_right, down_right = 'E', 'E', 'E'


        # no adjacent mines is revealed
        if top == top_right == right == down_right == down == down_left == left == top_left and top != 'M':
            board[i][j] = 'B'

            # recursively do 8 adjacents
            self.bfs_minesweeper(board, [i-1, j]) # top
            self.bfs_minesweeper(board, [i-1, j+1]) # top_right
            self.bfs_minesweeper(board, [i, j+1]) # right
            self.bfs_minesweeper(board, [i+1, j+1]) # down_right
            self.bfs_minesweeper(board, [i+1, j]) # down
            self.bfs_minesweeper(board, [i+1, j-1]) # down_left
            self.bfs_minesweeper(board, [i, j-1]) # left
            self.bfs_minesweeper(board, [i-1, j-1]) # top_left

        else: # at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
            num_mines = 0
            
            directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

            for direction in directions:
                m = direction[0]
                n = direction[1]
                try:
                    slot = board[i+m][j+n]  
                except:
                    slot = 'F'

                if slot == 'M':
                    num_mines += 1
                elif slot == 'E':
                    self.bfs_minesweeper(board, [ i+m, j+n ])

            # change digit
            board[i][j] = str(num_mines)

    







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
    

    # --------------- 529 ---------------
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'] ]

    click = [3,0]

    print(leetcode.updateBoard( board, click ))





