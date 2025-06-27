"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Floyd-Warshall Algorithm =========================================================
Floyd-Warshall class
Leetcode time
    1. Leetcode 1334: Find the City With the Smallest Number of Neighbors at a Threshold Distance

"""

import collections
from collections import defaultdict
from typing import List

class FloydWarshall:
    def __init__(self, V: int):
        self.V = V                                          # Number of vertices
        self.dist = [[float("inf")] * V for _ in range(V)]  # Distance matrix initialized to infinity
        self.path = [[-1] * V for _ in range(V)]            # Path matrix to reconstruct shortest paths

    def addEdge(self, u: int, v: int, weight: int):
        """Adds an edge (u → v) with given weight to the distance matrix."""
        self.dist[u][v] = weight                            # Set direct edge weight
        self.path[u][v] = u                                 # Set predecessor for shortest path reconstruction
        # Only set this if it's undirected graph
        self.dist[v][u] = weight
        self.path[v][u] = u

    def fw(self) -> bool:
        """Finds shortest paths between all pairs of vertices using Floyd-Warshall."""
        # Step 1: Set distance from each vertex to itself as 0
        for i in range(self.V):
            self.dist[i][i] = 0

        # Step 2: Iterate through all possible intermediate nodes
        for k in range(self.V):  # Intermediate vertex
            for i in range(self.V):  # Start vertex
                for j in range(self.V):  # End vertex
                    # If going through 'k' provides a shorter path from 'i' to 'j'
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]  # Update shortest distance
                        self.path[i][j] = self.path[k][j]  # Update path to reflect intermediate node

        # Step 3: Detect negative cycles (if any distance from a node to itself is negative)
        for i in range(self.V):
            if self.dist[i][i] < 0:
                print("Graph contains a negative-weight cycle.")
                return False

        return True  # No negative cycles detected

    def print_result(self):
        """Prints the shortest path distance matrix."""
        print("Shortest Distance Matrix:")
        for row in self.dist:
            print(row)

        print("Path Matrix:")
        for row in self.path:
            print(row)

    def print(self):
        print("Shortest Distance Matrix:")
        for row in self.dist:
            print(row)



class Solution:
    # Leetcode 1334: Find the City With the Smallest Number of Neighbors at a Threshold Distance
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize a fw obj and add all bidirectional edges
        fwObj = FloydWarshall(n)
        for edge in edges:
            u, v, w = edge
            fwObj.addEdge(u, v, w)
            fwObj.addEdge(v, u, w)

        # run the main algo
        fwBool = fwObj.fw()
        if not fwBool: return -1

        fwObj.print()

        # city -> # of neighbors with dist < distanceThreshold
        cityDict = collections.defaultdict(int)
        # record how many neighbors that satisfy the distanceThreshold each city has
        for row in range (n):
            for col in range (n):
                if fwObj.dist[row][col] != 0 and fwObj.dist[row][col] <= distanceThreshold:
                    cityDict[row] += 1
        print(cityDict)

        # find the min number of neighbor that a city has
        minNeighbor = float("inf")
        for city in range (n):
            minNeighbor = min(minNeighbor, cityDict[city])
        print(minNeighbor)

        # loop through the dict again to find the largest city with min # of neighbor
        result = -1
        for city in range (n):
            if cityDict[city] == minNeighbor:
                result = city

        return result





if __name__ == "__main__":
    """
    fw = FloydWarshall(5)
    fw.addEdge(0, 1, 6)
    fw.addEdge(0, 2, 7)
    fw.addEdge(1, 2, 8)
    fw.addEdge(1, 3, 5)
    fw.addEdge(1, 4, -4)
    fw.addEdge(2, 3, -3)
    fw.addEdge(2, 4, 9)
    fw.addEdge(3, 1, -2)
    fw.addEdge(4, 0, 2)
    fw.addEdge(4, 3, 7)

    fw = FloydWarshall(4)
    fw.addEdge(0, 1, 2)
    fw.addEdge(0, 3, 3)
    fw.addEdge(1, 0, 3)
    fw.addEdge(1, 2, 2)
    fw.addEdge(2, 3, 4)
    fw.addEdge(3, 1, 6)
    fw.addEdge(3, 0, -2)
    
    if fw.fw():
        fw.print_result()

    """

    solution = Solution()

    edges = [[1,2,619],[3,14,8975],[25,26,3132],[11,25,1931],[20,23,5266],[9,17,4907],[23,26,7013],[9,12,4077],[0,10,2575],[15,16,4541],[14,21,9643],[15,21,4366],[3,16,9007],[17,25,9582],[1,26,6137],[24,25,1755],[3,4,5892],[14,19,6961],[5,9,8298],[2,13,6947],[2,3,7393],[5,24,7850],[10,20,3662],[4,26,1611],[4,6,2897],[1,8,8471],[1,12,9758],[2,12,7393],[12,17,7653],[4,23,933],[1,19,1680],[17,19,1384],[10,23,6572],[11,19,6535],[16,19,4358],[13,14,3136],[11,24,8064],[4,10,9395],[7,18,5860],[9,13,9752],[7,11,6157],[13,21,8840],[13,25,8292],[3,13,1850],[11,12,9665],[1,4,204],[0,7,3890],[23,24,8006],[9,20,6314],[5,25,4310],[14,24,4370],[19,20,1397],[10,26,2657],[0,16,6455],[13,16,1607],[6,14,842],[5,15,3474],[6,7,5650],[2,10,2950],[3,17,2852],[5,20,4764],[12,26,9245],[10,24,1890],[10,12,3838],[4,17,243],[4,12,6854],[8,18,4721],[1,15,2571],[1,18,2390],[0,6,9497],[4,11,2187],[10,16,9962],[13,15,5370],[1,13,8980],[3,26,3118],[12,20,2016],[15,17,5478],[16,21,8087],[10,21,3310],[2,20,5118],[5,26,642],[15,22,9902],[15,24,3127],[12,13,2889],[7,9,5412],[0,8,8290],[4,13,3122],[4,24,3150],[19,25,6944],[20,22,1815],[5,14,5346],[12,14,9542],[2,4,9310],[21,25,4415],[10,14,2926],[14,15,43],[15,25,8248],[18,23,4969],[2,17,6272],[8,10,8835],[5,7,6324],[4,22,6624],[21,22,1041],[6,13,5195],[15,19,5505],[23,25,2209],[13,17,4246],[18,22,4386],[1,7,9946],[7,13,7232],[5,10,2617],[9,16,7556],[12,18,3138],[0,9,6287],[10,22,7690],[19,21,1532],[13,26,7247],[1,5,1996],[2,11,9147],[11,14,3064],[2,16,4212],[14,18,5072],[19,24,6723],[6,25,4822],[15,26,4893],[7,19,3267],[24,26,5851],[0,3,2135],[5,19,9783],[5,23,3523],[6,10,8838],[8,16,1707],[6,20,7064],[3,15,3552],[18,24,4293],[3,5,8753],[10,13,8762],[1,25,3879],[4,20,2163],[7,25,9244],[11,26,1116],[0,2,5525],[7,23,854],[0,13,7306],[9,14,4108],[2,25,960],[13,18,942],[6,26,9898],[11,21,4028],[4,8,601],[0,20,5804],[1,10,1523],[1,6,2770],[1,14,2958],[9,24,3139],[15,23,3073],[12,23,9992],[2,21,711],[7,12,8278],[8,13,8466],[6,21,189],[4,19,6694],[1,23,8096],[16,18,982],[1,11,8867],[5,17,3930],[16,22,8553],[3,24,3940],[2,7,1769],[1,3,5326],[11,16,6985],[1,21,2894],[6,12,528],[21,23,8444],[0,1,6332],[14,23,4995],[19,23,5799],[4,5,505],[0,4,7530],[5,18,5596],[9,11,6328],[20,21,7173],[16,24,8174],[15,20,7758],[16,17,5821],[7,15,2682],[7,16,7164],[12,24,1000],[7,20,8601],[8,24,5387],[17,24,4248],[8,11,9318],[14,17,787],[13,20,510],[0,25,6293],[3,22,2523],[7,26,7784],[17,23,3220],[4,16,6391],[8,22,8898],[0,24,9991],[3,23,7659],[8,15,2925],[8,19,3709],[12,22,8427],[16,23,977],[11,15,2695],[19,26,6737],[2,23,7427],[3,7,9537],[3,9,17],[8,14,3246],[12,15,761],[5,13,9281],[7,21,6497],[7,17,1208],[22,26,8624],[20,24,6591],[22,23,96],[17,22,2320],[22,24,3687],[8,20,6545],[22,25,5557],[5,12,3411],[14,16,1678],[4,15,6374],[14,26,5190],[8,17,538],[3,6,9807],[2,15,1256],[6,24,3310],[17,20,5737],[10,17,5767],[11,18,700],[3,20,7004],[4,25,9698],[0,15,5010],[1,9,7134],[9,22,4805],[7,10,8273],[1,17,2636],[11,13,2765],[13,24,8425],[18,19,9282],[13,19,2199],[6,8,207],[6,22,9343],[9,15,12],[18,20,7140],[2,14,3525],[17,21,3640],[5,16,7193],[10,15,1574],[8,12,124],[0,19,7149],[16,26,2611],[5,8,9001],[5,22,4718],[3,11,8461],[12,21,7571],[11,22,3046],[8,9,9382],[3,18,6401],[18,26,3148],[2,9,4753],[2,8,5191],[20,25,1883]]
    answer = solution.findTheCity(27, edges, 1939)
    print(answer)

