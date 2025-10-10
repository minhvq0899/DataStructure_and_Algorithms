"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

===================================================== Hierholzer’s algorithm for finding an Eulerian path =====================================================
Theory introduction: https://www.youtube.com/watch?v=8MpoO2zA2l4&ab_channel=WilliamFiset
Source code: https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/graphtheory/EulerianPathDirectedEdgesAdjacencyList.java

**Eulerian Path**: a path of edges that visits all the edges in a graph exactly once
1. Undirected graph: Either every vertex has even degree or exactly two vertics have odd degree. 
Those two vertices, if exists, will be the starting and ending point of the graph's Eulerian path
2. Directed graph: At most one vertex has (outdegree) - (indegree) = 1 and at most one vertext has (indegree) - (outdegree) = 1.
All other vertices have equal in and out degrees.
Vertex has (outdegree) - (indegree) = 1 will be our starting vertex
Vertex has (indegree) - (outdegree) = 1 will be our ending vertex

**Eulerian Circuit**: is an Eulerian path which starts and ends on the same vertex
1. Undirected graph: Every vertex has an even degree
2. Directed graph: every vertex has equal indegree and outdegree 

--> All vertices with non-zero degree need to belong to the same CC for the graph to have an Eulerian path/circuit

Hierholzer class
    __init__()
    get_eulerian_path()
    _setup()
    _has_eulerian_path()
    _find_start_node()
    _dfs()
    (static) initialize_empty_graph()
    (static) add_directed_edge()

    
Leetcode time - Leetcode class
    Leetcode 332. Reconstruct Itinerary
    Leetcode 2097. Valid Arrangement of Pairs

"""

from typing import List
from collections import deque, defaultdict

class Hierholzer_DirectedGraph:
    def __init__(self, graph):
        if graph is None:
            raise ValueError("Graph cannot be null")
        self.graph = graph
        self.n = len(graph)
        self.in_deg = [0] * self.n
        self.out_deg = [0] * self.n
        self.edge_count = 0
        self.path = []

    def get_eulerian_path(self):
        self._setup()

        if not self._has_eulerian_path():
            return None

        self._dfs(self._find_start_node())
        self.path.reverse()

        if len(self.path) != self.edge_count + 1:
            print("Eulerian Path doesn't exist. Path: ", self.path)
            return None

        return self.path

    # Populate in-degree, out-degree, and edge count
    def _setup(self):
        # Loop through each pair of u->u
        for from_node in range(self.n):
            for to_node in self.graph[from_node]:
                self.in_deg[to_node] += 1
                self.out_deg[from_node] += 1
                self.edge_count += 1
        
    # Helper function to check if a directed graph has an Eulerian path
    def _has_eulerian_path(self):
        if self.edge_count == 0:
            return False

        start_nodes = end_nodes = 0
        for i in range(self.n):
            diff = self.out_deg[i] - self.in_deg[i]
            # Case 1: If a vertex has a diff in in and out degree more than 1
            if diff > 1 or diff < -1:
                return False
            # Case 2: Potentially a start node
            elif diff == 1:
                start_nodes += 1
            # Case 3: Potentially an end node
            elif diff == -1:
                end_nodes += 1

        # Summarize the condition for a directed graph to have an Eulerian path
        return (start_nodes == 0 and end_nodes == 0) or (start_nodes == 1 and end_nodes == 1)

    # Vertex has (outdegree) - (indegree) = 1 will be our starting vertex
    def _find_start_node(self):
        start = 0
        for i in range(self.n):
            if self.out_deg[i] - self.in_deg[i] == 1:
                return i
            if self.out_deg[i] > 0:
                start = i
        return start

    # DFS to find the Eulerian path
    def _dfs(self, at):
        # Go down to the last vertex in our Eulerian path
        while self.out_deg[at] > 0:
            self.out_deg[at] -= 1
            next_node = self.graph[at][self.out_deg[at]]
            self._dfs(next_node)

        # Backtrack
        self.path.append(at)

    @staticmethod
    def initialize_empty_graph(n):
        return [[] for _ in range(n)]

    @staticmethod
    def add_directed_edge(graph, from_node, to_node):
        graph[from_node].append(to_node)


class FindEulerianPath332:
    def __init__(self, graph: defaultdict(list), n: int, num_edges: int):
        self.graph = graph  
        self.n = n                              # number of vertices
        self.in_degree = defaultdict(int)
        self.out_degree = defaultdict(int)
        self.num_edges = num_edges
        self.path = []

    # Populate in_degree and out_degree of each vertices
    def setUp(self):
        for v, neighbors in self.graph.items():
            for u in neighbors:
                self.in_degree[u] += 1
                self.out_degree[v] += 1

        # print(self.in_degree)
        # print(self.out_degree)

    # Main fn
    def getEulerianPath(self) -> List[str]:
        # Since LC 332 is guaranteed to have at least one valid itinerary and it starts from JFK,
        # we can skip step validate if graph has an Eulerian path and step finding the starting node
        self.setUp()
        if self.num_edges == 0:
            return None
        
        self.dfs("JFK")         # start out itinary from JFK
        self.path.reverse()

        if len(self.path) != self.num_edges + 1:
            return None
        
        return self.path
        
    def dfs(self, currentNode: str):
        while self.out_degree[currentNode] > 0:
            self.out_degree[currentNode] -= 1
            nextNode = self.graph[currentNode][self.out_degree[currentNode]]
            self.dfs(nextNode)

        self.path.append(currentNode)
        

class FindEulerianPath2097:
    def __init__(self, graph: defaultdict(list), n: int, num_edges: int):
        self.graph = graph
        self.n = n
        self.num_edges = num_edges
        self.in_degree = defaultdict(int)
        self.out_degree = defaultdict(int)
        self.paths = []

    # Populate in_degree and out_degree
    def setUp(self):
        for u, neighbors in self.graph.items():
            for v in neighbors:
                self.in_degree[v] += 1
                self.out_degree[u] += 1

    # Main fn
    def findEulerianPath(self) -> List[int]:
        # Skip validating if the graph actually has an Eulerian path
        self.setUp()

        # Find the starting node
        start = self.findStartingNode()

        # Compute the paths
        self.dfs(start)
        self.paths.reverse()

        if len(self.paths) != self.num_edges + 1:
            return None
        
        return self.paths        

    # Vertex has (outdegree) - (indegree) = 1 will be our starting vertex
    def findStartingNode(self) -> int:
        result = None
        for node, _ in self.graph.items():
            result = node
            if self.out_degree[result] - self.in_degree[result] == 1:
                return result
        
        return result   # If no node satisfies the above condition, any node can be starting node

    # DFS
    def dfs(self, currentNode: int):
        while self.out_degree[currentNode] > 0:
            self.out_degree[currentNode] -= 1
            nextNode = self.graph[currentNode][self.out_degree[currentNode]]
            self.dfs(nextNode)

        self.paths.append(currentNode)


class Leetcode:
    # Leetcode 332. Reconstruct Itinerary
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Graph representation
        graph = defaultdict(list)
        desinationSet = set()
        for u, v in sorted(tickets, reverse=True):
            desinationSet.add(u)
            desinationSet.add(v)
            graph[u].append(v)

        # Step 2: Set up in_degree and out_degree
        print("graph: ", graph)
        eulerian = FindEulerianPath332(graph = graph, n = len(desinationSet), num_edges = len(tickets))
        
        # Step 3: Compute our Eulerian path
        result = eulerian.getEulerianPath()
        print(result)

        return result


    # -------------------------------------------------------------------------------------------
    # Leetcode 2097. Valid Arrangement of Pairs
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Construct a graph
        graph = defaultdict(list)
        vertexSet = set()
        for u,v in pairs:
            graph[u].append(v)
            vertexSet.add(u)
            vertexSet.add(v)

        # Step 2: Construct the Eulerian path
        eulerian = FindEulerianPath2097(graph = graph, n = len(vertexSet), num_edges = len(pairs))
        eulerianPath = eulerian.findEulerianPath()

        # print(eulerianPath)

        # Step 3: Construct result
        result = []
        for i in range(len(eulerianPath)-1):
            result.append([eulerianPath[i], eulerianPath[i+1]])

        print(result)
        return result








if __name__ == "__main__":  
    def example_from_slides():
        n = 7
        graph = Hierholzer_DirectedGraph.initialize_empty_graph(n)

        edges = [
            (1, 2), (1, 3), (2, 2), (2, 4), (2, 4),
            (3, 1), (3, 2), (3, 5), (4, 3), (4, 6),
            (5, 6), (6, 3)
        ]

        for u, v in edges:
            Hierholzer_DirectedGraph.add_directed_edge(graph, u, v)

        solver = Hierholzer_DirectedGraph(graph)
        print(solver.get_eulerian_path())  # Output: [1, 3, 5, 6, 3, 2, 4, 3, 1, 2, 2, 4, 6]

    def small_example():
        n = 5
        graph = Hierholzer_DirectedGraph.initialize_empty_graph(n)

        edges = [(0, 1), (1, 2), (1, 4), (1, 3), (2, 1), (4, 1)]
        for u, v in edges:
            Hierholzer_DirectedGraph.add_directed_edge(graph, u, v)

        solver = Hierholzer_DirectedGraph(graph)
        print(solver.get_eulerian_path())  # Output: [0, 1, 4, 1, 2, 1, 3]

    # example_from_slides()
    # small_example()

    # ---------------------------------------------------------
    leetcode = Leetcode()

    # ------------- 332 -------------
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # # Output: ["JFK","ATL","JFK","SFO","ATL","SFO"] 
    # leetcode.findItinerary(tickets) 

    # ------------- 2097 -------------
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    leetcode.validArrangement(pairs)



