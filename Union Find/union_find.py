"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Union Find =========================================================

"""

from typing import List

class Union_by_rank():
    def findSetAndPathCompression(self, u, parent): 
        if parent[u] != u:
            parent[u] = self.findSetAndPathCompression(parent[u], parent)
        
        # this return will be first activated when we find the father
        return parent[u] 

    def unionByRank(self, u, v, parent, rank):
        u_parent = self.findSetAndPathCompression(u, parent)
        v_parent = self.findSetAndPathCompression(v, parent)

        # case 1: if they share a father
        if u_parent == v_parent:
            return

        # case 2: if they have different fathers
        if rank[u_parent] > rank[v_parent]:
            parent[v_parent] = u_parent
        elif rank[u_parent] < rank[v_parent]:
            parent[u_parent] = v_parent
        else: 
            # choose either one
            parent[v_parent] = u_parent
            rank[u_parent] += 1



















































