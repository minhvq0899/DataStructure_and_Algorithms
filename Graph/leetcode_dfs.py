"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Depth First Search =========================================================
1. Leetcode 17. Letter Combinations of a Phone Number
2. Leetcode 841. Keys and Rooms

"""
 
from typing import List

class Solution:
    # Leetcode 17. Letter Combinations of a Phone Number

    # Leetcode 841. Keys and Rooms
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # initialization
        visited = [ False for _ in range(len(rooms)) ]

        # dfs
        s = [0]
        visited[0] = True 
        cnt = 1

        while len(s):
            u = s.pop()
            for v in rooms[u]:
                if not visited[v]:
                    visited[v] = True
                    cnt += 1
                    s.append(v)

        print(visited)

        return cnt == len(rooms)
    


if __name__=="__main__":
    leetcode = Solution()
    
    # -------------- 841 --------------
    rooms = [ [1], [2], [3], [] ]
    access = leetcode.canVisitAllRooms(rooms)
    print(access)

    # -------------- 










