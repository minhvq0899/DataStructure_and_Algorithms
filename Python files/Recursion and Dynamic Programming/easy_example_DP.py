"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================= Examples for Recursion and Dynamic Programming =========================================
----------------- Leetcode 1025. Divisor Game -----------------
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.


----------------- Leetcode 263: Ugly Number -----------------
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.


"""

class Leetcode1025:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
        


class Leetcode263:
    # store known answers
    # everything in checkup[0] is True, everything in checkup[1] is False
    checkup = []
    checkup.append([1,2,3,4,5,6,8,9,10])
    checkup.append([0,7,11])
    
    def isUgly_DP_memoization(self, num: int) -> bool:
        two = True if num % 2 == 0 else False
        three = True if num % 3 == 0 else False
        five = True if num % 5 == 0 else False

        # if the answer is already stored, simply return it
        if num in self.checkup[0]: return True
        elif num in self.checkup[1]: return False
        
        if five:
            if self.isUgly(num/5):
                # save this answer so we do not have to compute it again
                self.checkup[0].append(num) 
                return True
            else: 
                self.checkup[1].append(num)
                return False
        elif three: 
            if self.isUgly(num/3):
                self.checkup[0].append(num) 
                return True
            else: 
                self.checkup[1].append(num)
                return False
        elif two: 
            if self.isUgly(num/2):
                self.checkup[0].append(num) 
                return True
            else: 
                self.checkup[1].append(num)
                return False
        
    def isUgly_fast(self, num: int) -> bool:
        # if num == 0
        if num < 1: return False
        
        # if num is ugly, it must be a product of either 2,3, or 5
        # just divide num by 5,3,2 until you cannot divide anymore
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        
        # if in the end you get 1, that means it IS a product of only 2,3 and 5
        if num == 1:
            return True
        
        return False


if __name__ == "__main__":
    ugly = Leetcode263()
    print("Final answer: ", ugly.isUgly(1000))
    print(ugly.checkup)










