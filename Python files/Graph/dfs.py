"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Depth First Search =========================================================

"""

from typing import List


# DFS
def dfs(start: int):
    s = [start]
    visited[start] = True
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                s.append(v)


# DFS using recursion
# Does NOT guarantee to yeild the same result as DFS using list
def dfs_recursive(start: int):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            path[v] = start
            dfs_recursive(v)



def printPath(start: int, end: int) -> str:
    trace = [end]
    while end != start:
        end = path[end]
        trace.append(end)
    
    trace.reverse()

    return "->".join( [str(item) for item in trace] )


# detect a cycle in directed graph
class Cycle_proton:
    detectCycle = False
    # init
    def __init__(self, graph, visited):
        self.graph = graph
        self.visited = visited

    # detect a cycle in directed graph
    def cycle(self, start: int):
        for v in self.graph[start]:
            if self.visited[v] == 0:
                self.visited[v] = 1
                self.cycle(v)
            elif self.visited[start] == 1:
                self.detectCycle = True
            
            self.visited[v] = 2

    












if __name__ == "__main__":    
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 2),
        (5, 1),
        (5, 4),
        (4, 6)
    ]
    

    # vertices
    V = 7

    # three list we need
    graph = [[] for _ in range(V)]
    visited = [0 for _ in range(V)]
    path = [-1 for _ in range(V)]

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        # graph[v].append(u)

    # ----------------------------------------------------
    """
    print(graph,  "\n")  
    print("Before ", path, "\n")  

    dfs(0)
    print("After using normal dfs ", path, "\n")

    # ---------------------------------
    visited = [False for _ in range(V)]
    path = [-1 for _ in range(V)]

    dfs_recursive(0)
    print("After using recursive dfs", path, "\n")
    
    # print(printPath(0, 6))

    # --------------------------------
    visited = [False for _ in range(V)]
    cycle(0)
    print("Cycle? ", detechCycle)
    """

    # ----------------------------------------------------
    # visited = [False for _ in range(V)]

    #cycle = Cycle_160(graph, visited)
    #cycle.cycle_160()
    #print( cycle.hasCycle() )

    # ----------------------------------------------------
    cycle = Cycle_proton(graph, visited)
    cycle.cycle(0)
    print( cycle.detectCycle )


