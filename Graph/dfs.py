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


detechCycle = False
# detect a cycle in directed graph
def cycle(start: int):
    for v in graph[start]:
        if visited[v] == 0:
            visited[v] == 1
            cycle(v)
        elif visited[start] == 1:
            detectCycle = True
    
    visited[v] = 2


# Class cycle in CSCI 160
class Cycle_160:
    hasCycleboo = False

    def __init__(self, graph, visited):
        self.graph = graph
        self.visited = visited

    # detech a cycle from 160
    def cycle_160(self):
        for i in range (len(self.graph)):
            if not self.visited[i]:
                self.dfs_160(i, i)

    # dfs
    def dfs_160(self, start: int, end: int):
        self.visited[start] = True
        for v in self.graph[start]:
            if not self.visited[v]:
                self.dfs_160(v, start) 
            elif v == end:
                self.hasCycleboo = True
    
    # has cycle
    def hasCycle(self):
        return self.hasCycleboo













if __name__ == "__main__":    
    """
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (4, 3),
        (4, 2),
        (5, 1),
        (5, 4),
        (4, 6)
    ]
    """

    edges = [
        (0, 1),
        (1, 2), 
        (2, 0)
    ]

    # vertices
    V = 7

    # three list we need
    graph = [[] for _ in range(V)]
    visited = [False for _ in range(V)]
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

    cycle = Cycle_160(graph, visited)
    cycle.cycle_160()
    b = cycle.hasCycle()
    print( b )



