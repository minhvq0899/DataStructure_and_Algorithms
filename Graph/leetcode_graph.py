"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Graph =========================================================

1. Leetcode 997. Find the Town Judge
2. Leetcode 1042. Flower Planting With No Adjacent

"""

from typing import List
import collections

class Solution:
    # Leetcode 997. Find the Town Judge
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusts = [ [] for _ in range (N+1) ] 
        trusted = [ [] for _ in range (N+1) ]

        for rela in trust:
            trust_er = rela[0]
            trust_ee = rela[1]
            # person at index i trust following people
            trusts[trust_er].append(trust_ee)
            # person at index i is trusted by following people
            trusted[trust_ee].append(trust_er)

        potential = []
        for i in range (1, N+1):
            # if someone trusts nobody, he/she is a suspect
            if len(trusts[i]) == 0:
                potential.append(i)
        
        for poten in potential:
            # if a suspect is trusted by everyone, he/she is the judge
            if len(trusted[poten]) == (N-1):
                return poten

        return -1

    # Leetcode 1042. Flower Planting With No Adjacent
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # store all edges in a list of length n+1 (edges[0] is empty)
        edges = [ [] for _ in range (n+1) ]

        # edges[i] store all connecting edges
        for path in paths: # O(n)
            v1, v2 = path
            # bidirectional edge
            edges[v1].append(v2)
            edges[v2].append(v1)
        
        # a dict to store which flower has been planted in which garden
        flower_dict = collections.defaultdict(int)
        # go through each garden
        for i in range (1, n+1): # O(n)
            # a set of all possible type of flower
            aSet = {1,2,3,4}
            # connecting_edges contains all edges connect to garden i
            connecting_edges = edges[i]
            # loop through each edge to delete all types of flower which 
            # has already been planted in other gardens
            for con_edge in connecting_edges:
                if flower_dict[con_edge] != 0:
                    aSet.discard( flower_dict[con_edge] )
            # plant a type of flower in garden i
            flower_dict[i] = aSet.pop()
            
        ans = [None] * n
        for k, v in flower_dict.items(): # O(n)
            ans[k-1] = v

        return ans






if __name__ == "__main__":
    leetcode = Solution()

    # ------------------------------------------------------------------
    #lc997 = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    #N = 4

    #jugde = leetcode.findJudge(N, lc997)            
    # print("Judge: ", jugde)

    # ------------------------------------------------------------------
    lc1042 = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    n = 4

    ans = leetcode.gardenNoAdj(n, lc1042)
    print(ans)












