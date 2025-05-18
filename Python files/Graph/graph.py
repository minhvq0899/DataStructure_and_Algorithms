"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Graph =========================================================

"""

edges = [
    [0, 1],
    [0, 2],
    [2, 1],
    [1, 4], 
    [4, 2],
    [2, 3],
    [3, 0],
    [5, 6],
    [6, 7]
]


vertice = 8
connection = 9

# Or if you don't have the access to vertice and connection
# connection = len(edges)
# count = 0
# aSet = set()
# for edge in edges:
#     u, v = edge
#     aSet.add(u)
#     aSet.add(v)
# vertice = len(aSet)


import collections

graph = collections.defaultdict(list)

"""
defaultdict(list): for dictionary with value as lists

Why should we use defaultdict(list) instead of regular dictionary? 
Because when we access a key that does not exist in defaultdict, 
it gives back an empty list instead of an error like regular dictionary

"""

for edge in edges:
    u, v = edge
    graph[u].append(v)

print(graph)



