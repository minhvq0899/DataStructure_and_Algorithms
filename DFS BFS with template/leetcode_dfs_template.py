"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= DFS with template =========================================================
DFS down different path: 
    1. Leetcode 22. Generate Parentheses
    2. Leetcode 752. Open the Lock

DFS on grid/ matrix
    1. Leetcode 417. Pacific Atlantic Water Flow
    2. Leetcode 1020. Number of Enclaves


"""

from collections import deque
from typing import List

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
        
    
    # Leetcode 752. Open the Lock
    def openLock(self, deadends: List[str], target: str) -> int:
        # if each time you checks for deadends, you have to iterates through a list, it will be O(n)
        # instead, store you deadends in a set
        deadendsSet = {deadend for deadend in deadends}
        
        # create a data structure to store answers
        potential = []
        # create count and seen set
        seen = set()
        count = 0

        # call DFS
        self.dfs_openLock([0,0,0,0], deadendsSet, target, potential, count, seen)

        print("Potential: ", potential)
        return min(potential) if potential else -1


    def dfs_openLock(self, current: List[int], deadends: set, target: str, potential: List[int], count: int, seen: set):
        # base cases
        currentStr = ""
        for digit in current:
            currentStr += str(digit)
        print(currentStr)

        if currentStr in deadends: # if the current combination is in deadend
            print("Deadendddddddd")
            return
        if currentStr in seen: # if the current combination has already been seen
            print("Seen\n\n")
            return 
        if currentStr == target: # if target is found
            potential.append(count)
            return 

        # TO DO
        count += 1
        seen.add(currentStr)

        # Call DFS where needed
        for i in range (len(current)):
            if current[i] == 9:
                # go up
                current[i] = 0
                self.dfs_openLock(current, deadends, target, potential, count, seen)
                # go down
                current[i] = 8
                self.dfs_openLock(current, deadends, target, potential, count, seen)
            elif current[i] == 0:
                # go up 
                current[i] = 1
                self.dfs_openLock(current, deadends, target, potential, count, seen)
                # go down
                current[i] = 9
                self.dfs_openLock(current, deadends, target, potential, count, seen)
            else: 
                # go up
                current[i] += 1
                self.dfs_openLock(current, deadends, target, potential, count, seen)
                # go down
                current[i] -= 2
                self.dfs_openLock(current, deadends, target, potential, count, seen)
       
            

   

    # ========================================================================================================================================= 




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


    # --------------------------------
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

    # -------------------------------------------








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
    target = "6000"

    print( leetcode.openLock(deadends, target) )












