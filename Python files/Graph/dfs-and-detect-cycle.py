"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Depth First Search =========================================================

"""

from typing import List
import collections
from collections import defaultdict


""" Class DFS """
class DFS:
    def __init__(self, graph: collections.defaultdict(list), V: int):
        self.graph = graph
        self.visited = [False for _ in range (V)]
        self.path = [-1 for _ in range (V)]

    def dfs_iterative(self, start: int):
        # create a stack
        s = [start]
        self.visited[start] = True
        while len(s) > 0:
            u = s.pop()
            for v in self.graph[u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.path[v] = u
                    s.append(v)

    # DFS using recursion
    # Does NOT guarantee to yeild the same result as iterative DFS
    def dfs_recursive(self, start: int):
        self.visited[start] = True
        for v in self.graph[start]:
            if not self.visited[v]:
                self.path[v] = start
                self.dfs_recursive(v)

    def printPath(self, start: int, end: int) -> str:
        trace = [end]
        while end != start:
            end = self.path[end]
            trace.append(end)
        
        trace.reverse()

        return "->".join( [str(item) for item in trace] )



""" Detect a cycle in directed graph """
class CycleDirectedGraph:
    # init
    def __init__(self, graph: collections.defaultdict(list), V: int):
        self.graph = graph
        self.visited = [0 for _ in range (V)]   # 0 = unvisited, 1 = visiting, 2 = visited
        self.cycle = False

    # Directed graphs can have multiple components. 
    # For example, if your graph has three separate "islands" of connected nodes and you only start DFS from one, 
    # the other components won’t be visited — meaning any cycles in them remain undetected.
    def detectCycleOneComponent(self, start: int):
        self.visited[start] = 1         # mark as visiting

        for v in self.graph[start]:
            if self.visited[v] == 0:
                self.detectCycleOneComponent(v)
                if self.cycle: 
                    return              # exit early 
            elif self.visited[v] == 1:  # a back edge found (v is already on the recursion stack)
                self.cycle = True
                return
            
        self.visited[start] = 2         # mark node as fully processed


    # detect a cycle in the WHOLE directed graph
    def detectCycle(self):
        for v in range (len(self.visited)):
            if self.visited[v] == 0:
                self.detectCycleOneComponent(v)
                if self.cycle:
                    return True     # exit early
        return False



""" Helper to detect cycle in undirected graph using DFS """
class CycleUndirectedGraph:
    def __init__(self, graph: collections.defaultdict(list), V: int): 
        self.graph = graph
        self.visited = [False for _ in range(V)]

    # detect a cycle in the WHOLE directed graph
    def detectCycle(self) -> bool:
        # Iterates through all nodes to ensure disconnected components are also checked.
        # Returns True if any component contains a cycle.
        for i in range(len(self.visited)):
            if not self.visited[i]:
                if self.dfs(i, -1):  # -1 as parent of root
                    return True
        return False

    def dfs(self, vertex: int, parent: int) -> bool:
        # Standard DFS. Marks the current node as visited.
        # A cycle is found if we revisit a node that's already visited and not the parent.
        self.visited[vertex] = True

        for neighbor in self.graph[vertex]:
            if not self.visited[neighbor]:
                if self.dfs(neighbor, vertex): 
                    return True
            elif neighbor != parent:        # case where we already found visited 'neighbor'
                # We've found a back edge → cycle
                return True

        return False














if __name__ == "__main__":    
    edges = [
        (0, 1),
        (0, 3),
        (3, 2),
        (2, 4),
        (3, 4)
    ]

    # vertices
    V = 5

    # prepare graph
    directed_graph = collections.defaultdict(list)
    undirected_graph = collections.defaultdict(list)
    visited = [0 for _ in range(V)]
    path = [-1 for _ in range(V)]

    for edge in edges:
        u, v = edge
        directed_graph[u].append(v)
        undirected_graph[u].append(v)
        undirected_graph[v].append(u)

    # ----------------------------------------------------
    dfsClass = DFS(directed_graph, V)
    cycleDirectedGraph = CycleDirectedGraph(directed_graph, V)
    cycleUndirectedGraph = CycleUndirectedGraph(undirected_graph, V)

    # Find cycle in Directed graph
    cycleDirectedGraph.detectCycle()
    print( cycleDirectedGraph.cycle )

    # Find cycle in Undirected graph
    print( cycleUndirectedGraph.detectCycle() )


