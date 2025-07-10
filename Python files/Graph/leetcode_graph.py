"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Graph =========================================================

1. Leetcode 997. Find the Town Judge
2. Leetcode 1042. Flower Planting With No Adjacent
==========================================
Graph Template
3. Leetcode 323. Number of CC in an Undirected Graph
4. Leetcode 207. Course Schedule - Detect Cycle in Directed Graph
5. Leetcode 261. Graph Valid Tree - Detect Cycle in Undirected Graph
    Helper function to detect cycle in undirected graph using DFS
6. Leetcode 332. Reconstruct Itinerary

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


    # ---------------------------------------------------------------------------------------
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


    # ---------------------------------------------------------------------------------------
    # Leetcode 323: Number of CC in an Undirected Graph
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # -------------------------- set up graph --------------------------
        # a special dict: <int, List[int]>
        graph = collections.defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        # ------------------------------------------------------------------

        visited = [False for _ in range(n)]         # visited boolean
        count = 0

        # attempt to DFS from each vertice, so we can find the different CCs
        for i in range(n):
            if visited[i] == False:
                count += 1                          # found a CC
                self.CC_dfs(graph, visited, i)
        
        return count


    # iterative
    def CC_dfs(self, graph: collections.defaultdict(list), visited: List[bool], vertice: int):
        stack = [vertice]
        visited[vertice] = True

        while stack:                                # while stack is not empty
            u = stack.pop()
            for v in graph[u]:
                if visited[v] == False:
                    visited[v] = True
                    stack.append(v)


    # ---------------------------------------------------------------------------------------
    # Leetcode 207: Course Schedule - Detect Cycle in Directed Graph
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize graph
        graph = [[] for _ in range (numCourses)]
        for pre in prerequisites:
            v, u = pre
            graph[u].append(v)
        
        visited = [0 for _ in range (numCourses)]
        hasCycle = False
        # ------------------------------------
        # check for cycle
        def cycle(start):
            for v in graph[start]:
                if visited[v] == 0:
                    visited[v] = 1
                    cycle(v)
                elif visited[v] == 1:
                    nonlocal hasCycle
                    hasCycle = True
                
                visited[v] = 2
        # ------------------------------------
        # check cycle from each node
        for i in range (numCourses):
            cycle(i)

        return not hasCycle



    # -------------------------------------------------------------------------------------
    # Leetcode 261: Graph Valid Tree - Detect Cycle in Undirected Graph
    # Write a function that returns true if a given undirected graph is tree and false otherwise
    # An undirected graph is tree if it has following properties. 
    #       1) There is no cycle. 
    #       2) The graph is connected.
    def graphValidTree(self, n: int, edges: List[List[int]]) -> bool:
        # ========== Step 1: Set up graph ==========
        graph = collections.defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False for _ in range(n)]

        # ========== Step 2: Detect cycle and Step 3: Detect connectivity ==========
        hasCycle = False
        count = 0

        for i in range(n):
            if visited[i] == False:
                count += 1
                hasCycle = hasCycle or self.cycle_undirected_dfs(graph, visited, i, -1)
        
        return not hasCycle and count == 1


    # -------------------------------------------------------------------------------------
    def cycle_undirected_dfs(self, graph: collections.defaultdict(list), visited: List[bool], vertice: int, parent: int) -> bool:
        visited[vertice] = True

        for v in graph[vertice]:
            if visited[v] == False:
                if self.cycle_undirected_dfs(graph, visited, v, vertice): 
                    return True
            elif v != parent: 
                return True
    
        return False





    # -------------------------------------------------------------------------------------
    # Leetcode 6. Leetcode 332. Reconstruct Itinerary
    # Hierholzer’s algorithm for finding an Eulerian path
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # ========== Step 1: Build the graph ==========
        # Sort tickets in reverse lex order so we can pop the smallest destination last
        graph = collections.defaultdict(list)
        for ticket in sorted(tickets, reverse=True):
            u, v = ticket
            graph[u].append(v)

        for departure, arrival in enumerate(graph):
            print("{}: {}".format(departure, arrival))

        # ========== Step 2: DFS traversal using stack ==========
        stack, result = [], []  # stack for backtracking, result for final itinerary
        stop = "JFK"            # start from JFK as required

        while stop:
            if not graph[stop]:
                # No more outgoing flights from this airport
                # Add to result as part of final itinerary
                result.append(stop)

                # Backtrack to previous airport
                stop = stack.pop() if stack else None
            else:
                # Still have destinations to explore
                # Push current airport to stack and go deeper
                stack.append(stop)
                stop = graph[stop].pop()  # pop the lex smallest destination (due to reverse sort)

        # Reverse the result to get the correct order (since we built it post-order)
        return result[::-1]









if __name__ == "__main__":
    leetcode = Solution()

    # ------------------------------------------------------------------
    #lc997 = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    #N = 4

    #jugde = leetcode.findJudge(N, lc997)            
    # print("Judge: ", jugde)

    # ------------------------------------------------------------------
    # lc1042 = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    # n = 4

    # ans = leetcode.gardenNoAdj(n, lc1042)
    # print(ans)

    # ------------------------------------------------------------------
    # N = 6
    # edges = [ [0,1], [1,2], [2,0], [3,4] ]
    # print( leetcode.countComponents(N, edges) )

    # ------------------------------------------------------------------
    N = 12
    edges = [ [0,1],[1,2],[2,3],[0,6],[2,4],[1,5],[0,7],[7,8],[8,9],[7,11],[11,10] ]
    print(leetcode.graphValidTree(N, edges)) # True

    # ------------------------------------------------------------------
    # N = 10
    # edges = [ [0,1],[1,2],[1,5],[2,3],[3,4],[4,2],[4,6],[7,8],[8,9] ]
    # print(leetcode.countComponents_test(N,edges))





