"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Union Find =========================================================
1. Leetcode 547. Number of Provinces
2. Leetcode 684. Redundant Connection
3. Leetcode 1319. Number of Operations to Make Network Connected
"""

from union_find import *

class Solution:
    # Union Find
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
            potential = self.unionByRank_684(u, v, parents, rank)
            if potential: # if the returning edge is not empty
                redundant_edges.append(potential)
        
        print(redundant_edges)
        return redundant_edges.pop() # return the last edge




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

# ====================================================================================================================

    # Leetcode 529. Minesweeper
    def adjacentMines(self, board: List[List[str]], click: List[int]) -> int:
        i, j = click
        
        num_mines = 0
        for r in range (i-1, i+2):
            for c in range (j-1, j+2):
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                    if board[r][c] == "M":
                        num_mines += 1

        return num_mines
                    

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        If click on "M" 
            -> game over
        else if click on "E"
            if no adjacent mines
                reveal it as "B"
            else
                digit 1->8
        
        """
        i, j = click
        
        # 1. If a mine ('M') is revealed, then the game is over - change it to 'X'
        if board[i][j] == 'M': 
            board[i][j] = 'X'
        # 2. If an empty square ('E') is revealed
        else: 
            # compute number of adjacent mines
            num_mines = self.adjacentMines(board, click)
            if num_mines: 
                board[i][j] = str(num_mines)
            else: 
                board[i][j] = "B"
                for r in range (i-1, i+2):
                    for c in range (j-1, j+2):
                        if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] != "B":
                            self.updateBoard(board, [r, c])
                
        return board


    # -----------------------------------------------------------------------

    # Leetcode 17. Letter Combinations of a Phone Number
    def letterCombinations(self, digits: str) -> List[str]:
        # create a data strucutre to store answers
        ans = []

        if digits != None and len(digits) > 0:
            mapping = ["", "", "abc", "def", "ghi", "jkl","mno","pqrs","tuv","wxyz"]
            d = digits[0] # if digits == "23" then d == "2"
            letters = mapping[ int(d) ] # letters == "abc"
            for char in letters:     
                self.dfs(digits, mapping, ans, 1, char)
            
        return ans

    def dfs(self, digits: str, mapping: List[str], ans: List[str], index: int, potential: str):
        # base cases: we found 1 combination
        if len(potential) == len(digits):
            ans.append(potential)
            return 
            
        # variation
        d = digits[index] # d == 2
        letters = mapping[ int(d) ]
        for char in letters:
            self.dfs(digits, mapping, ans, index + 1, potential + char)

    # -----------------------------------------------------------------------------------------

    # Leetcode 752. Open the Lock
    def openLock(self, deadends: List[str], target: str) -> int:
        # create a DS to store answer
        min_turn = 0

        # initialize dfs/ bfs
    
    def bfs_openLock(self, )



                








if __name__ == "__main__":
    leetcode = Solution()

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

        

















