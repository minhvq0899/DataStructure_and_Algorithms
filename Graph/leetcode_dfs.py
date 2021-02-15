"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Depth First Search =========================================================
1. Leetcode 841. Keys and Rooms
2. Leetcode 200. Number of Islands
3. Leetcode 207. Course Schedule
4. Leetcode 210. Course Schedule II

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

        return cnt == len(rooms)

    # -------------------------------------------------------------------------------------

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
    

    # -------------------------------------------------------------------------------------


    # Leetcode 207. Course Schedule
    # Detect cycle in a directed graph
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize graph
        graph = [[] for _ in range (numCourses)]
        for pre in prerequisites:
            v, u = pre
            graph[u].append(v)
        
        visited = [0 for _ in range (numCourses)]
        hasCycle = False

        # check for cycle
        def cycle(start):
            for v in graph[start]:
                if visited[v] == 0:
                    visited[v] = 1
                    cycle(v)
                elif visited[v] == 1:
                    nonlocal hasCycle
                    hasCycle = True
                
                visited[v] = 2
        
        # check cycle from each node
        for i in range (numCourses):
            cycle(i)

        return not hasCycle



    # Leetcode 210. Course Schedule II
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        











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


    # --------------- 210 ---------------






