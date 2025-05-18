"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Breadth First Search =========================================================

"""

from typing import List
import queue

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 2),
    (5, 1),
    (5, 4),
    (4, 6),
]

# vertices
V = 7

# three list we need
graph = [[] for _ in range(V)]
visited = [False for _ in range(V)]
path = [-1 for _ in range(V)]
q = queue.Queue()
for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)
# print(graph)


# BFS
def bfs(s: int):
    # mark that we have visited start
    visited[s] = True
    # put start into queue
    q.put(s)

    # kepp running while until the queue is empty
    while q.qsize() > 0:
        u = q.get() # pop the queue
        # check all the vertices connected to u
        for v in graph[u]:
            if not visited[v]: # if v has not been visited yet
                visited[v] = True
                path[v] = u # mark the path to v is u
                q.put(v) # put v into the queue
    

# trace back
def printPath(start: int, end: int) -> str:
    shortest_path = [end]
    while path[end] != start:
        end = path[end]
        shortest_path.append(end)

    shortest_path.append(start)
 
    shortest_path.reverse() # easier to visualize
    
    return "->".join( [str(item) for item in shortest_path] )


if __name__ == "__main__":
    # for bfs
    bfs(0)
    print(path)

    # for printPath()
    print(printPath(1, 6))

