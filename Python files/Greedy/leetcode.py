"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================= Leetcode Exercises Sorting Algorithms =========================================
1. Leetcode 860. Lemonade Change
2. Leetcode 455. Assign Cookies
3. Leetcode 1276. Number of Burgers with No Waste of Ingredients

"""

from typing import List

class Solution:
    # Leetcode 860. Lemonade Change
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = { 5: 0, 10: 0, 20: 0 }

        for bill in bills:
            # if they pay $20
            if bill == 20:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[20] += 1
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[20] += 1
                    wallet[5] -= 3
                else: 
                    return False
            # if they pay $10
            elif bill == 10:
                if wallet[5] > 0:
                    wallet[10] += 1
                    wallet[5] -= 1
                else:
                    return False
            else: # if bill == 5
                wallet[5] += 1
        
        return True

    # Leetcode 455. Assign Cookies
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j = 0, 0

        while i < len(g) and j < len(s):
            if s[j] < g[i]:
                j += 1
            else: 
                i += 1
                j += 1
        
        return i + 1


    # Leetcode 1276. Number of Burgers with No Waste of Ingredients
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        '''
        x = jumbo burger, y = small burger
        4x + 2y = tomatoSlices
        x + y = cheeseSlides  <=>  4x + 4y = 4cheeseSlides
        '''

        '''
        jumbo = (4*cheeseSlices - tomatoSlices) / 2
        small = cheeseSlices - jumbo

        if jumbo.is_integer():
            return [int(jumbo), int(small)]

        return []
        '''

        # use tomatoSlides to find cheeseSlides
        # binary search

        i = 0
        j = cheeseSlices

        while i <= j:
            y = (i + j) // 2 # number of small burger
            x = cheeseSlices - y # number of jumbo burger

            if 4 * x + 2 * y < tomatoSlices:
                # we want to increase the tomatoSlides -> increase jumbo -> decrase small
                # because x + y = cheese --> one more small means one less jumbo
                j = y - 1
            elif 4 * x + 2 * y > tomatoSlices:
                # we want to decrease tomatoSlides
                i = y + 1
            else: 
                return [x, y]
            
        return []








if __name__ == "__main__":
    leetcode = Solution()

    # ---------------------------------------------------------------
    # lc860 = [5,5,5,10,20]
    # print(leetcode.lemonadeChange(lc860))

    # ---------------------------------------------------------------
    lc455 = [[1,2,3], [1,1]]
    print(leetcode.findContentChildren(lc455[0], lc455[1]))





