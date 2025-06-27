"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Union Find =========================================================
0. Union Find
    def findSetAndPathCompression(self, u: int, parent: List[int]):
    def unionByRank(self, u: int, v: int, parent: int, rank: List[int]):

1. Leetcode 547. Number of Provinces
2. Leetcode 684. Redundant Connection
3. Leetcode 1319. Number of Operations to Make Network Connected
4. Leetcode 261: Graph Valid Tree - Detect Cycle in Undirected Graph

"""

from union_find import *
import collections

class Solution:
    # Union Find
    def findSetAndPathCompression(self, u: int, parent: List[int]): 
        if parent[u] != u:
            parent[u] = self.findSetAndPathCompression(parent[u], parent)
        
        # this return will be first activated when we find the father
        return parent[u] 

    def unionByRank(self, u: int, v: int, parent: int, rank: List[int]):
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
    

    # --------------------------------------------------------------------------------------
    # Leetcode 547. Number of Provinces
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # initialization
        n = len(isConnected)
        rank = [0 for _ in range (n)]
        parents = [i for i in range (n)]
        
        for j in range (n):
            for i in range (j):
                if isConnected[i][j] == 1:
                    self.unionByRank(i, j, parents, rank)
        
        # count how many father nodes
        cnt = 0
        for i in range (n):
            if parents[i] == i:
                cnt += 1
        
        return cnt


    # --------------------------------------------------------------------------------------
    # Leetcode 684. Redundant Connection
    def unionByRank_find_redundant(self, u, v, parent, rank) -> List[int]:
        u_parent = self.findSetAndPathCompression(u, parent)
        v_parent = self.findSetAndPathCompression(v, parent)

        # case 1: if they share a father -> they are already in the same group and this connection is redundant
        if u_parent == v_parent:
            return [u, v]

        # case 2: if they have different fathers
        if rank[u_parent] > rank[v_parent]:
            parent[v_parent] = u_parent
        elif rank[u_parent] < rank[v_parent]:
            parent[u_parent] = v_parent
        else: 
            # choose either one
            parent[v_parent] = u_parent
            rank[u_parent] += 1
        
        return []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # len(edges) is the number of edges == number of vertices - 1
        # however, we have 1 too many edges => number of vertices == len(edges)
        N = len(edges) 
        parents = [i for i in range (N+1)]
        rank = [0 for _ in range (N+1)]

        # have a list of possible redundant edges
        redundant_edges = []

        # do union find with all edges
        for edge in edges:
            u, v = edge
            potential = self.unionByRank_find_redundant(u, v, parents, rank)
            if potential: # if the returning edge is not empty
                redundant_edges.append(potential)
        
        print(redundant_edges)
        return redundant_edges.pop() # return the last edge


    # --------------------------------------------------------------------------------------
    # Leetcode 1319. Number of Operations to Make Network Connected 
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        We can compute redundant connections and number of groups 
        If the number of redundant connections is >= number of groups - 1
        --> Possible

        Ex: 3 groups and 2 redundant connections -> possible
        """
        rank = [0 for _ in range (n)]
        parents = [i for i in range (n)]
        # Compute the number of redundant connections
        redundant_connections = []

        # Compute number of groups
        for con in connections:
            u, v = con
            potential = self.unionByRank_find_redundant(u, v, parents, rank)
            if potential: # if the returning edge is not empty
                redundant_connections.append(potential)

        # Count how many father nodes
        group = 0
        for i in range (n):
            if parents[i] == i:
                group += 1
        
        # If the number of redundant connections is >= number of groups - 1
        # --> Possible
        if len(redundant_connections) >= group-1:
            return group-1
        else:
            return -1


    # -------------------------------------------------------------------------------------
    # Leetcode 261: Graph Valid Tree - Detect Cycle in Undirected Graph
    # Write a function that returns true if a given undirected graph is tree and false otherwise
    # An undirected graph is tree if it has following properties. 
    #       1) There is no cycle. 
    #       2) The graph is connected.
    # We can do this with Union Find providing that there is no self loop (Ex: [0,0])
    # helper function to detect cycle in an undirected graph using Union Find
    def unionByRank_detect_cycle(self, u: int, v: int, parent: List[int], rank: List[int]) -> bool:
        u_parent = self.findSetAndPathCompression(u, parent)
        v_parent = self.findSetAndPathCompression(v, parent)

        # If the two vertices share the same father, providing that there is no 
        # duplicate in connection, a cycle is detected. Union-find cannot detect self loop
        if u_parent == v_parent:
            return True
        if rank[u_parent] > rank[v_parent]:
            parent[v_parent] = u_parent
        elif rank[v_parent] > rank[u_parent]:
            parent[u_parent] = v_parent
        else:
            parent[v_parent] = u_parent
            rank[u_parent] += 1
        
        return False

    # Union Find edition
    def graphValidTree(self, n: int, edges: List[List[int]]) -> bool:
        # ========== Step 1: Set up Union Find ==========
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        # ========== Step 2: Detect cycle and Step 3: Connectivity ==========
        hasCycle = False
        for edge in edges:
            u, v = edge
            hasCycle = hasCycle or self.unionByRank_detect_cycle(u, v, parent, rank)
            
        group = 0
        for i in range(n):
            if i == parent[i]: group += 1
        
        return not hasCycle and group == 1


# ================================================================================================


   




if __name__ == "__main__":
    leetcode = Solution()

    # ------ Union by Rank ------
    # connections = [[3,1], [7,5], [10,7], [11,10], [9,8], [5,0], [4,2], [8,4], [6,3]]
    # N = 11
    # parent = [i for i in range(N+1)]
    # rank = [0 for _ in range(N+1)]

    # for conn in connections:
    #     son, father = conn
    #     leetcode.unionByRank(son, father, parent, rank)

    # ---------------------------
    # province = leetcode.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
    # print(province)

    # ---------------------------
    # redundant = leetcode.findRedundantConnection([[1,2], [1,3], [2,3]])
    # print(redundant)

    # ---------------------------
    # leetcode1319 = leetcode.makeConnected(4, [[0,1],[0,2],[1,2]])
    # print(leetcode1319)

    # ---------------------------
    # board = [['E', 'E', 'E', 'E', 'E'],
    #          ['E', 'E', 'M', 'E', 'E'],
    #          ['E', 'E', 'E', 'E', 'E'],
    #          ['E', 'E', 'E', 'E', 'E'] ]
    # click = [3, 0]

    # mine = leetcode.updateBoard(board, click)
    # expected = [['B', '1', 'E', '1', 'B'],
    #             ['B', '1', 'M', '1', 'B'],
    #             ['B', '1', '1', '1', 'B'],
    #             ['B', 'B', 'B', 'B', 'B'] ]

    # assert mine == expected

    # ------------------------------
    # digits = "23"
    # combinations = leetcode.letterCombinations(digits)
    # print(combinations)

    # ------------------------------
    N = 12
    edges = [ [0,1],[1,2],[2,3],[0,6],[2,4],[1,5],[0,7],[7,8],[8,10],[8,9],[7,11],[11,10] ]
    print(leetcode.graphValidTree(N, edges)) # True
        

















