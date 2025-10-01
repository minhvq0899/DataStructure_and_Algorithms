"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Union Find =========================================================
Union Find
    def findSetAndPathCompression(self, u: int, parent: List[int]):
    def unionByRank(self, u: int, v: int, parent: int, rank: List[int]):

Leetcode 547. Number of Provinces
Leetcode 684. Redundant Connection
Leetcode 1319. Number of Operations to Make Network Connected
Leetcode 261: Graph Valid Tree - Detect Cycle in Undirected Graph
Leetcode 947. Most Stones Removed with Same Row or Column
Leetcode 1361. Validate Binary Tree Nodes
Leetcode 1101. The Earliest Moment When Everyone Become Friends
Leetcode 721. Accounts Merge

(Hard)
Leetcode 305. Number of Islands II

"""

from union_find import *
import collections

class UnionFind1361:
    def __init__(self, n: int):
        self.parents = [i for i in range (0, n)]
        # self.rank = [0] * n

    def findParentAndPathCompression(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.findParentAndPathCompression(self.parents[u])

        return self.parents[u]

    def union(self, u: int, v: int) -> bool:
        u_parent = self.findParentAndPathCompression(u)
        v_parent = self.findParentAndPathCompression(v)

        # Case 1: if they share a parent -> Cycle detected
        if u_parent == v_parent:
            return False

        # Case 2: if they don't share a parent -> just pick u
        self.parents[v_parent] = u_parent
        return True



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

    # ------------------------------------------------------------------------------------- 
    # Leetcode 947. Most Stones Removed with Same Row or Column
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parents = defaultdict()
        for i in range(n):
            parents[i] = i

        uf = Union_by_rank(n, parents)

        # If stones share a row or column, union them
        for i in range(n):
            for j in range(i+1, n):
                stone1 = stones[i]
                stone2 = stones[j]
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    uf.unionByRank(i, j)
        
        # print(uf.parents)
        # Count how many stones are their own parents
        parents = 0
        for stone, parent in uf.parents.items():
            if stone == parent:
                parents += 1

       # The number of stones can be removed will be the complement 
        # (n - # of components)
        return n - parents


    # ------------------------------------------------------------------------------------- 
    # Leetcode 1361. Validate Binary Tree Nodes
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ufClass = UnionFind1361(n)
        has_parent = [False] * n                                # Track if a node already has a parent

        for parent in range (n):
            # print(ufClass.parents)
            for child in (leftChild[parent], rightChild[parent]):
                if child != -1:
                    if has_parent[child]:                       # Multiple parents 
                        return False                

                    has_parent[child] = True

                    if not ufClass.union(parent, child):            # Cycle detected
                        return False

        # A valid tree must have nodes with only one parent and exactly one node with no parent
        # Count nodes with no parent — should be exactly one (the root)
        root_count = has_parent.count(False)

        # Here, we don't have to check if the rest of the node share the same parent 0, because we are sure they do
        # If one of them have a different parent, that parent will be another node without a parent, meaning root_count should be 2 in this case
        return root_count == 1
   
    # ------------------------------------------------------------------------------------- 
    # Leetcode 1101. The Earliest Moment When Everyone Become Friends
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda log: log[0])

        unionFind = Union_by_rank(n)
        components = n

        # Tweaking the 'union' API to return True if successfully union two components
        for timeStamp, u, v in logs:
            if unionFind.unionByRank(u, v):
                components -= 1
            
                if components == 1:
                    return timeStamp

        return -1

    # ------------------------------------------------------------------------------------- 
    # Leetcode 721. Accounts Merge
    # The idea is to Union accounts with each other. Initially, each account has itself as parent.
    # First, have 'emailToIdMap' mapping. Loop through each email, if that email is already in the mapping, union two account ID.
    # Finally, have 'parentAccountIdToEmails' to store result. For each email, we know the accountID that email belongs to. 
    # Find the parent acount ID of that accountID, then add the email to the parent accound ID list.
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = defaultdict(int)              # Initially, each account will have itself as parent
        for index, account in enumerate(accounts):
            parents[index] = index
        
        uf = Union_by_rank(len(accounts), parents)
        emailToIdMap = defaultdict(int)         # Account ID will be the account index in "accounts" input

        # Loop through each email in the list. If that email is already in our mapping, union two accound IDs together
        for index, account in enumerate(accounts):
            for i in range(1, len(account)):
                email = account[i]
                if email in emailToIdMap:
                    uf.unionByRank(index, emailToIdMap[email])
                else:
                    emailToIdMap[email] = index
            
        # print(emailToIdMap)
        # print(uf.parents)
        # print(uf.rank)

        # Loop through each email and find all the emails that belong to the same union
        parentAccountIdToEmails = defaultdict(list)     # parent account ID (int) -> [email1, email2, etc]
        for email, accountID in emailToIdMap.items():
            parentAccountID = uf.findSetAndPathCompression(accountID)       # find parent account
            parentAccountIdToEmails[parentAccountID].append(email)          # add that email to the union

        # print(parentAccountIdToEmails)
        
        # Prepare result in the format the problem requires
        results = []
        for parentAccountId, l in parentAccountIdToEmails.items():
            name = accounts[parentAccountId][0]
            l.sort()
            result = [name] + l
            results.append(result)

        # print(results)
        return results
        


    # =====================================================================================
    # Leetcode 305. Number of Islands II
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Initialize parents dict. Every cell is its own parent
        parents = defaultdict(int)
        for r in range(m):
            for c in range(n):
                index = r*n + c
                parents[index] = index

        uf = Union_by_rank(m*n, parents)
        islands = set()
        numberIsland = 0
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for rp, cp in positions:
            positionIndex = rp * n + cp

            # If this cell is already an island
            if positionIndex in islands:
                result.append(numberIsland)
                continue

            islands.add(positionIndex)          # Add this new island to set
            numberIsland += 1

            # Check if any neighbor is a land
            for ar, ac in directions:
                nr = rp + ar
                nc = cp + ac
                if 0 <= nr < m and 0 <= nc < n:
                    neighborIndex = nr * n + nc
                    # If yes, union current position with that neighbor
                    if neighborIndex in islands:
                        # If we successfully union two lands, the number of land decrement by 1
                        if uf.unionByRank(positionIndex, neighborIndex):
                            numberIsland -= 1

            result.append(numberIsland)

        return result












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
    # N = 12
    # edges = [ [0,1],[1,2],[2,3],[0,6],[2,4],[1,5],[0,7],[7,8],[8,10],[8,9],[7,11],[11,10] ]
    # print(leetcode.graphValidTree(N, edges)) # True
        
    # ------------------------------
    # n = 4
    # leftChild = [1,-1,3,2]
    # rightChild = [2,3,-1,-1]
    # print(leetcode.validateBinaryTreeNodes(n, leftChild, rightChild))

    # ------------------------------
    # stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    # leetcode.removeStones(stones)

    # ------------------------------
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    leetcode.accountsMerge(accounts)















