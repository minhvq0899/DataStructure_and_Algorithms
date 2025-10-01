"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Leetcode Graph =========================================================

Leetcode 997. Find the Town Judge
Leetcode 1042. Flower Planting With No Adjacent
=========================================
Graph Template
    ** Directed graph **
Leetcode 207. Course Schedule - Detect Cycle in Directed Graph
Leetcode 1361. Validate Binary Tree Nodes (Same approach as 261)
Leetcode 802. Find Eventual Safe States
    
    ** Undirected graph **
Leetcode 323. Number of CC in an Undirected Graph
Leetcode 261. Graph Valid Tree - Detect Cycle in Undirected Graph
Leetcode 399. Evaluate Division

    ** Array-based problem **
Leetcode 3551. Minimum Swaps to Sort by Digit Sum - https://www.geeksforgeeks.org/dsa/minimum-number-swaps-required-sort-array/#

"""

from typing import List
import collections
import math

class checkCycleAndCcInUndirectedGraph:
    def __init__(self, graph: List[List[int]], n: int):
        self.graph = graph
        self.numV = n
        self.cc = 0
        self.cycleExist = False

    def cycle(self):
        visited = [False for _ in range(self.numV)]
        # -----------------------------
        def dfs(node: int, parent: int):
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, node)
                else:   # if 'neighbor' is already visited
                    if neighbor != parent:
                        self.cycleExist = True
        # -----------------------------

        # DFS from each unvisited node
        for i in range(self.numV):
            if not visited[i]:
                visited[i] = True
                self.cc += 1
                dfs(i, -1)

class cycleDetection802:
    def __init__(self, graph, numV):
        self.graph = graph
        self.V = numV
        

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


    """ Directed graph """
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
    # Leetcode 1361. Validate Binary Tree Nodes
    # Same idea as above problem 261, a valid Binary Tree should have the following properties:
    #   1) DAG - Directed Acyclic Graph
    #   2) Graph is connected
    #   3) Each node has at most one parent
    #   4) Only one node doesn't have a parent (root) => must have exactly one root
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Graph repre and track parent count
        graph = collections.defaultdict(list)
        inDegree = [0] * n
        for parent in range (n):
            for child in ( [leftChild[parent], rightChild[parent]] ):
                if child == -1: continue

                graph[parent].append(child)
                
                # Increment the number of node pointing to child
                inDegree[child] += 1
                # Validate 3) Each node has at most one parent
                if inDegree[child] > 1:     
                    return False
        print(graph)

        # Validate 4) must have exactly one root
        roots = [i for i in range (len(inDegree)) if inDegree[i] == 0]
        if len(roots) != 1: 
            return False
        root = roots[0]

        # Validate 1) No cycle
        visited = [0] * n
        cycle = False
        # Just have to DFS from root
        cycle = cycle or self.detectCycleInDirectedGraph(graph, root, visited)
        
        if cycle: 
            return False

        # After DFS from root, if there is a node that is still unvisited, then it's from a different component
        for i in range (len(visited)):
            if not visited[i]: return False
        
        return True    

    def detectCycleInDirectedGraph(self, graph, start, visited) -> bool:
        # mark start as visiting
        visited[start] = 1

        for neighbor in graph[start]:
            if visited[neighbor] == 0:
                self.detectCycleInDirectedGraph(graph, neighbor, visited)
            elif visited[neighbor] == 1:
                return True
            
        # complete eximining 
        visited[start] = 2
        return False


    # -------------------------------------------------------------------------------------
    # Leetcode 802. Find Eventual Safe States
    # Goal is to identify all nodes that are not part of any cycle in a directed graph
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0] * len(graph)      # 0 = not visited, 1 = visiting, 2 = visted/safe (not part of any cycle)
        # ----------------------------------
        def cycleDetectionDfs(node) -> bool:
            # If node in also on the current recursion stack, meaning this is a cycle
            if visited[node] == 1:
                return True
            elif visited[node] == 2:
                return False
            
            # Once we are here, it means 'node' is not visited yet -> mark as visiting
            visited[node] = 1

            # DFS on all node's neighbors
            for neighbor in graph[node]:
                if cycleDetectionDfs(neighbor):
                    return True
                
            # Eventually, if node is not part of a cycle, mark visited[node] as 2
            visited[node] = 2

            return False
        # ----------------------------------
        # if a node is part of a cycle, visited[node] will never be 2
        result = []
        for i in range(len(graph)):
            if not cycleDetectionDfs(i):
                result.append(i)

        return result

    """ Undirected graph """
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

    # -------------------------------------------------------------------------------------
    # Leetcode 261: Graph Valid Tree - Detect Cycle in Undirected Graph
    # Write a function that returns true if a given undirected graph is tree and false otherwise
    # An undirected graph is tree if it has following properties: 
    #       1) There is no cycle. 
    #       2) The graph is connected.
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Step 1: Graph representation
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Run Cycle detection
        cycleObject = checkCycleAndCcInUndirectedGraph(graph, n)
        cycleObject.cycle()
        
        return (not cycleObject.cycleExist) and (cycleObject.cc == 1)

    
    # -------------------------------------------------------------------------------------
    # Leetcode 399. Evaluate Division
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)       # vertice -> [[vertice, multiply weight], ...]
        
        # Populate the undirected graph
        for index, equation in enumerate(equations):
            # u/v = value  -->  u = value * v and v = u * (1/value)
            u, v = equation         
            value = values[index]
            graph[u].append([v, value])
            graph[v].append([u, 1/value])

        # Now, we do BFS for each pair of queries
        # ------------------------------
        def bfs(source, target) -> float:
            visited = set()            
            dq = collections.deque()
            dq.append((source, 1))

            while dq:
                popNode, popWeight = dq.popleft()
                for neighbor, neighborWeight in graph[popNode]:
                    if neighbor not in visited:
                        if neighbor == target:
                            return popWeight * neighborWeight
                        
                        visited.add(neighbor)
                        dq.append((neighbor, popWeight * neighborWeight))

            return -1.0
        # ------------------------------
        results = []
        for u, v in queries:
            results.append(bfs(u, v))

        # print(results)
        return results

            



    """ Array-based problem """
    # -------------------------------------------------------------------------------------
    # Leetcode 3551. Minimum Swaps to Sort by Digit Sum
    def minSwaps_arraySolution(self, nums: List[int]) -> int:
        # Our nums_temp will contain (digitSum, nums[i], i)
        nums_temp = []
        indexDict = collections.defaultdict(int)    # nums[i] -> i
        for i in range(len(nums)):
            num = nums[i]
            indexDict[num] = i
            digitSum = 0
            while math.floor(num / 10) != 0:
                digitSum += num % 10
                num = math.floor(num/10)
            
            digitSum += num % 10
            nums_temp.append( (digitSum, nums[i], i) )      

        nums_temp.sort()    
        # print(nums_temp)
        # print(nums)

        # Count number of swap
        swap = 0
        for i in range(len(nums_temp)):
            currentDigitSum, currentNum, currentIndex = nums_temp[i]
            
            while currentIndex != i:
                # Swap
                nums_temp[i], nums_temp[currentIndex] = nums_temp[currentIndex], nums_temp[i]
                swap += 1
                currentDigitSum, currentNum, currentIndex = nums_temp[i]

        # print(swap)
        return swap

    def minSwaps_cycleDetectionSolution(self, nums: List[int]) -> int:
        # Our nums_temp will contain (digitSum, nums[i], i)
        nums_temp = []
        indexDict = collections.defaultdict(int)    # nums[i] -> i
        for i in range(len(nums)):
            num = nums[i]
            indexDict[num] = i
            digitSum = 0
            while math.floor(num / 10) != 0:
                digitSum += num % 10
                num = math.floor(num/10)
            
            digitSum += num % 10
            nums_temp.append( (digitSum, nums[i], i) )      

        nums_temp.sort()  

        # As we traverse it, if an element hasn’t been visited and isn’t in its correct position,
        # we trace the cycle formed by the misplaced elements and find its size
        # The swap count is then updated by cycleSize - 1
        visited = [False] * len(nums_temp)
        swap = 0
        for i in range(len(nums_temp)):
            currentDigitSum, currentNum, currentIndex = nums_temp[i]
            # If current element is already visited or already in the correct position
            if visited[i] or currentIndex == i:
                continue

            j, cycleSize = i, 0
            # We make a cycle until it comes back to first element again.
            while not visited[j]:
                currentDigitSum, currentNum, currentIndex = nums_temp[j]
                visited[j] = True

                # Move to the next element of the cycle
                j = indexDict[currentNum]
                cycleSize += 1

            # Update answer
            if cycleSize > 0:
                swap += (cycleSize-1)

        print(swap)
        return swap




    












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
    # N = 12
    # edges = [ [0,1],[1,2],[2,3],[0,6],[2,4],[1,5],[0,7],[7,8],[8,9],[7,11],[11,10] ]
    # print(leetcode.graphValidTree(N, edges)) # True

    # ------------------------------------------------------------------
    # N = 10
    # edges = [ [0,1],[1,2],[1,5],[2,3],[3,4],[4,2],[4,6],[7,8],[8,9] ]
    # print(leetcode.countComponents_test(N,edges))

    # ------------------------------------------------------------------
    # n = 4
    # leftChild = [1,0,3,-1]
    # rightChild = [-1,-1,-1,-1]
    # print(leetcode.validateBinaryTreeNodes(n, leftChild, rightChild))

    # -------------------------- 3551 --------------------------
    # nums = [18,43,34,16]
    # leetcode.minSwaps_cycleDetectionSolution(nums)

    # -------------------------- 399 --------------------------
    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    leetcode.calcEquation(equations, values, queries)