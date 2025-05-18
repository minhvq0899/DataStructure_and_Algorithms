"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Breadth First Search =========================================================
1. Leetcode 690. Employee Importance
2. Leetcode 1129. Shortest Path with Alternating Colors
3. Leetcode 752. Open the Lock

"""

from typing import List
import queue

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
    

















if __name__ == "__main__":
    leetcode = Solution()

    # ---------------------------------
    # n = 3
    # red_edges = [[0,1]]
    # blue_edges = [[1,2]]

    # distance = leetcode.shortestAlternatingPaths(n, red_edges, blue_edges)
    # print(distance)

    # -------------------------------------------
    deadends = ["0201","0101","0102","1212","2002"] 
    target = "0202"

    min_turns = leetcode.openLock(deadends, target)
    print(min_turns)



