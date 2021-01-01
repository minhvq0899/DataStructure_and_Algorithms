"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

============================================================ Stack ============================================================

1. 

"""

from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        temp = [res for res in restaurants if res[2] >= veganFriendly]
        temp1 = [res for res in temp if res[3] <= maxPrice]
        temp = [res for res in temp1 if res[4] <= maxDistance]

        temp.sort(key = lambda x: [-x[1], -x[0]])    

        return [res[0] for res in temp]



if __name__ == "__main__":
    array = Solution()

    lc1333 = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
    print(filter(lc1333, 1, 50, 50))










