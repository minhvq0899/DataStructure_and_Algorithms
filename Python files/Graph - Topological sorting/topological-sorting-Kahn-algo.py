"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Topological Sorting Algorithm =========================================================
TopologicalSorting class
Leetcode time
    Leetcode 210. Course Schedule II 
    Leetcode 310: Minimum Height Trees 
    Leetcode 444. Sequence Reconstruction (Premium)
    Leetcode 1136: Parallel Courses (Premium)
    Leetcode 1857. Largest Color Value in a Directed Graph (Hard)
    Leetcode 269. Alien Dictionary (Premium + Hard)

"""

from typing import List
from collections import defaultdict, deque
import collections

class TopologicalSorting:
    def __init__(self, graph: defaultdict(list), V: int):
        self.graph = graph  # Directed graph: node -> list of neighbors
        self.V = V          # Number of vertices

    def kahn(self) -> bool:
        """Performs topological sorting using Kahn’s algorithm.
        Returns True if a valid sort exists (i.e., no cycle), False otherwise."""
        in_degree = [0] * self.V  # Tracks incoming edge count for each node

        # Step 1: Compute in-degree for each node
        for u in range(self.V):
            for v in self.graph[u]:
                in_degree[v] += 1

        print("Original in-degree array: ", in_degree)

        # Step 2: Initialize queue with all nodes having in-degree 0
        queue = deque([i for i in range(self.V) if in_degree[i] == 0])
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1  # Remove edge u → v
                if in_degree[v] == 0:
                    queue.append(v)

        # If we processed all nodes, we have a valid topological ordering
        if len(topo_order) == self.V:
            print("Topological Order:", topo_order)
            return True
        else:
            print("Cycle detected. No valid topological ordering.")
            print("Incorrect topo order: ", topo_order)
            return False
        

        




class Solution: 
    # Leetcode 210. Course Schedule II -------------------------------------------------------------------------------------------
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Going to use Kahn's algo for Topo sorting"""
        # Step 1: Create graph and in_degree list for all nodes
        graph = collections.defaultdict(list)
        in_degree = [0 for _ in range (numCourses)]
        for pre in prerequisites:
            a, b = pre
            graph[b].append(a)
            in_degree[a] += 1

        # Step 2: Initialize a queue with all nodes having in-degree of 0
        queue = collections.deque( [i for i in range (numCourses) if in_degree[i] == 0] )
        #print(queue)

        # Step 3: Repreatedly remove node from the graph until all nodes are processed
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for neighbor in graph[u]:
                in_degree[neighbor] -= 1        # remove edge u -> neighbor
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        print(topo_order)

        if len(topo_order) == numCourses:
            return topo_order
        
        return []  


    # Leetcode 310: Minimum Height Trees -----------------------------------------------------------------------------------------
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Corner case
        if n == 1:
            return [0]
        
        # Step 1: Create a undirected graph. in_degree can be inferred from the graph
        graph = defaultdict(set)
        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)

        # Step 2: Initialize a queue with all the leave nodes
        queue_leaves = deque( [i for i in range (n) if len(graph[i]) == 1] )
        numNodes = n

        # Step 3: Trim leaves
        while numNodes > 2:
            # Update number of nodes
            numLeaves = len(queue_leaves)
            numNodes -= numLeaves                       
            
            print(queue_leaves)
            for _ in range (len(queue_leaves)):
                leaf = queue_leaves.popleft()
                neighbor = graph[leaf].pop()            # graph[leaf] should only have one element left
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    queue_leaves.append(neighbor)
        
        # print(queue_leaves)
        return list(queue_leaves)
 

    # 1857. Largest Color Value in a Directed Graph ------------------------------------------------------------------------------
    # https://algo.monster/liteproblems/1857
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Step 1: graph representation
        n = len(colors)
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)

        # Step 2: Build a topological sorting for this graph
        # Step 3: Dynamic Programming
        # 2.1. Construct the in_degree array
        topo_order = []
        in_degree = [0 for _ in range (n)]
        for edge in edges:
            u, v = edge
            in_degree[v] += 1

        # 3.1. Construct a 2D memo
        # memo[node][c] will represents the max count of color c appears on any path ending at node i
        memo = [defaultdict(int) for _ in range (n)]
        result = 0          # store the largest color value of any valid path

        # 2.2. Initialize the queue
        dq = deque([node for node in range (n) if in_degree[node] == 0])
        print(dq)

        # 2.3. Run Kahns algorithm
        # 3.2. Populate the 2D array 'memo'
        # memo = [{r:1},{r:1, p:1},{r:2},{b:1,r:2},{r:3,b:1}] 
        while dq:
            # topo order
            pop = dq.popleft()
            topo_order.append(pop)
            # update memo
            popColor = colors[pop:pop+1]
            popColorDict = memo[pop]
            popColorDict[popColor] += 1
            # update 'result'
            for c, freq in popColorDict.items():
                result = max(result, freq)

            for neighbor in graph[pop]:
                # remove edge pop->neighbor
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    dq.append(neighbor)
                # update memo
                neighborColorDict = memo[neighbor]
                for c, freq in popColorDict.items():
                    neighborColorDict[c] = max(neighborColorDict[c], freq)

        print("memo: ", memo)
        print("topo_order: ", topo_order)

        # 2.4. Check for cycle
        if len(topo_order) < n:
            return -1
        
        return result


    # Leetcode 269. Alien Dictionary ---------------------------------------------------------------------------------------------
    def alienOrder(self, words: List[str]) -> str:
        charSet = set()
        for word in words:
            for char in word:
                charSet.add(char)

        # Step 1: Graph representation
        graph = defaultdict(list)

        # Logic to create a graph from a list of lexicographically sorted words
        # Think about how words are sorted lexicographically - comparing each chat at a time
        for wordIndex in range (len(words) - 1):
            w1, w2 = words[wordIndex], words[wordIndex+1]
            maxCharIndex = min( len(w1), len(w2) )

            # Edge cases
            if w1[:maxCharIndex] == w2[:maxCharIndex] and len(w1) > len(w2):
                return ""

            # Loop through each char in two adj words
            for charIndex in range (maxCharIndex):
                if w1[charIndex] != w2[charIndex]:
                    graph[w1[charIndex]].append(w2[charIndex])
                    break

        print("graph: ", graph)

        # Step 2: Run Kahns Topological order algo
        in_degree = defaultdict(int)
        for _ , dest in graph.items():
            for node in dest:
                in_degree[node] += 1

        dq = deque([char for char in charSet if in_degree[char] == 0])
        print("dq: ", dq)

        topo_order = ""
        while dq:
            pop = dq.popleft()
            topo_order += pop

            for neighbor in graph[pop]:
                # remove edge pop->neighbor
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    dq.append(neighbor)
        
        if len(topo_order) < len(charSet):
            return ""
                
        return topo_order

            







if __name__ == "__main__":    
    """
    # Example usage
    V = 14                                  # Number of vertices
    graph = defaultdict(list)
    graph[0] = [2,3]
    graph[1] = [4]
    graph[2] = [6]
    graph[3] = [1,4]
    graph[4] = [5,8]
    graph[6] = [7,11, 0]
    graph[7] = [4,12]
    graph[9] = [2,10]
    graph[10] = [6]
    graph[11] = [12]
    graph[12] = [8]

    ts = TopologicalSorting(graph, V)

    print(ts.kahn())
    """
    # =====================================================================
    leetcode = Solution()

    # Leetcode 310: Minimum Height Trees --------------------------------------------------------------------------------------------
    # edges = [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[6,8],[8,9],[9,10]]
    # answer310 = leetcode.findMinHeightTrees(11, edges)
    # print(answer310)

    # Leetcode 1857. Largest Color Value in a Directed Graph ------------------------------------------------------------------------------
    # colors = "abaca"
    # edges = [[0,1],[0,2],[1,2],[2,3],[3,4]]
    # answer = leetcode.largestPathValue(colors, edges)
    # print("Leetcode 1857. Largest Color Value in a Directed Graph: ", answer)

    # Leetcode 269. Alien Dictionary ---------------------------------------------------------------------------------------------
    # words = ["wrt","wrf","er","ett","rftt"]
    words = ["z", "z"]
    # words = ["abc", "ab"]
    answer = leetcode.alienOrder(words)
    print("Leetcode 269. Alien Dictionary: ", answer)





