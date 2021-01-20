"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Breadth First Search =========================================================
1. Leetcode 690. Employee Importance


"""

from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    # Leetcode 690. Employee Importance
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # to store the graph in format
        # {id: object}
        graph = {}
        for emp in employees:
            graph[emp.id] = emp
        
        # initialize a queue
        q = queue.Queue()
        q.put(id)
        
        # BFS
        count = graph[id].importance
        while q.qsize() > 0:
            u = q.get()
            vertices = graph[u].subordinates
            for v in vertices: # list of all subordinates of u
                q.put(v)
                count += graph[v].importance
        
        return count











if __name__ == "__main__":
    



