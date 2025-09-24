"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Union Find =========================================================

"""

from typing import List
from collections import defaultdict

class Union_by_rank():
    def __init__(self, n: int, parentDict: defaultdict(int)):
        self.rank = [1] * n
        self.parents = parentDict
        
    def findSetAndPathCompression(self, u: int) -> int: 
        if self.parents[u] != u:
            self.parents[u] = self.findSetAndPathCompression(self.parents[u])
        
        # this return will be first activated when we find the father
        return self.parents[u]

    # Return True if one node's parent just got modified (# of components decremented by 1)
    def unionByRank(self, u: int, v: int) -> bool:
        u_parent = self.findSetAndPathCompression(u)
        v_parent = self.findSetAndPathCompression(v)

        # After finding the parents, only work on the parents now
        # case 1: if they share a father
        if u_parent == v_parent:
            return False

        # case 2: if they have different fathers
        if self.rank[u_parent] > self.rank[v_parent]:
            self.parents[v_parent] = u_parent
            self.rank[u_parent] += self.rank[v_parent]
        else: 
            self.parents[u_parent] = v_parent
            self.rank[v_parent] += self.rank[u_parent]

        return True



















































