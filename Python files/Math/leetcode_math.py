"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Math  =========================================================
1. Leetcode 360: Sort Transformed Array
2. Leetcode 264. Ugly Number II
3. Leetcode 12. Integer to Roman
4. Leetcode 1154. Day of the Year
5. Leetcode 367. Valid Perfect Square
6. Leetcode 1375. Bulb Switcher III
7. Leetcode 1227. Airplane Seat Assignment Probability
8. Leetcode 1033. Moving Stones Until Consecutive

"""


from typing import List


# Leetcode exercises
class Solution:
    # Leetcode 360: Sort Transformed Array
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        '''
        Given a sorted array of integers nums and int a,b,c. Apply quadratic fn of the form:
        f(x) = ax^2 + bx + c for x in nums
        The return array must be sorted
        Expected time complexity: O(n)

        Idea: 
        Compute -b/2a
        Resut array y = []
        Based on the position of -b/2a in nums to arrage elements in y
        1. Create 2 smaller arrays: left and right
        2. If a > 0: left is decreasing, right is increasing 
        -> reverse left, compute f(x) for both arrays, merge 2 arrays
        3. If a < 0: left is increasing, right is decreasing 
        -> reverse right, compute f(x) for both arrays, merge 2 arrays
        return the merged array

        This will result in O(n) for time complexity
        '''
        # helper fn to compute quadratic fn
        def quadratic_fn(a, b, c, x) -> int:
            return a*(x**2) + b*x + c

        # -b/2a
        pivot = -b / (2*a)
        # now pop all x that are larger than pivot
        right = []
        pop = nums.pop()
        if pop <= pivot:
            nums.append(pop)
        else:
            while (pop > pivot):
                right.append(pop)
                pop = nums.pop()
            nums.append(pop)

        # now we have right and nums as left
        # now right is being reversed
        right.reverse()

        # apply the increasing and decreasing theory of quadratic fn
        if a > 0: 
            nums.reverse()
        else:
            right.reverse()

        # compute quadratic fn for both nums and right: O(n)
        for i in range (len(nums)):
            nums[i] = quadratic_fn(a, b, c, nums[i])
        for i in range (len(right)):
            right[i] = quadratic_fn(a, b, c, right[i])

        print(nums, "       ", right)

        # now merge those two arrays: O(n) 
        result = []
        i, j = 0, 0
        while (i < len(nums) or j < len(right)):
            if i < len(nums) and j < len(right):
                if nums[i] < right[j]:
                    result.append( nums[i] )
                    i += 1
                else: 
                    result.append( right[j] )
                    j += 1
            elif i >= len(nums):
                result.append(right[j])
                j += 1
            else:
                result.append( left[i] )
                i += 1
        
        return result



    # ----------------------------------------------------------------------------------
    # Leetcode 264. Ugly Number II
    def nthUglyNumber(self, n: int) -> int:
        '''
        O(n)
        Any ugly number must be in one of these three sequence
        (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
        (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
        (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
        '''
        # initialize stored array
        ugly = [None] * n
        ugly[0] = 1
        
        # initialize 3 index pointers
        i2, i3, i5 = 0, 0, 0 
        
        # Assume you have Uk, the kth ugly number. 
        # Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5), with L1, L2, L3 
        # be three of the previous ugly numbers (can be Uk+1)
        next_multiple_of_2 = ugly[i2] * 2
        next_multiple_of_3 = ugly[i3] * 3
        next_multiple_of_5 = ugly[i5] * 5
        
        # loop to that n-th ugly number we need
        for i in range (1, n):
            ugly[i] = min(next_multiple_of_2,
                          next_multiple_of_3,
                          next_multiple_of_5)
            # we prioritize i2, meaning if there is an ugly number can be
            # computed by two number (ex: 10 = 2*5 and 5*2), we prioritize 
            # increasing the small number (2)
            if ugly[i] == next_multiple_of_2: 
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            
            if ugly[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            
            if ugly[i] == next_multiple_of_5: 
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
        
        return ugly[-1]
                


    # ----------------------------------------------------------------------------------
    # Leetcode 12. Integer to Roman
    def intToRoman(self, num: int) -> str:
        value =      [1000, 900, 500, 400, 100, 90, 50,  40, 10,  9,   5,  4,   1]
        roman_char = ['M', 'CM', 'D','CD', 'C','XC','L','XL','X','IX','V','IV','I']

        result = ''
        for i in range ( len(value) ):
            while num >= value[i]:
                result += roman_char[i]
                num -= value[i]
        
        return result



    # ----------------------------------------------------------------------------------
    # Leetcode 1154. Day of the Year
    def dayOfYear(self, date: str) -> int:
        normal_month_mapping = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_month_mapping = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        date = date.split('-')
        # helper function -----------------------------------
        def leapYear(year) -> bool:
            if year % 4 == 0:
                if year % 100 == 0:
                    return True if year % 400 == 0 else False
                else:
                    return True
            return False
        # ---------------------------------------------------
        year = int( date[0] )
        month = int( date[1] )
        number_of_days = 0

        if leapYear(year):
            for i in range (month):
                number_of_days += leap_month_mapping[i]
        else: 
            for i in range (month):
                number_of_days += normal_month_mapping[i]

        number_of_days += int( date[2] )

        return number_of_days



    # ----------------------------------------------------------------------------------
    # Leetcode 367. Valid Perfect Square
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l < r:
            mid = (l + r) // 2
            if mid*mid > num:
                r = mid - 1
            elif mid*mid < num:
                l = mid + 1
            else:
                return True
        
        return False
        


    # ----------------------------------------------------------------------------------
    # Leetcode 1375. Bulb Switcher III
    def numTimesAllBlue(self, light: List[int]) -> int:
        num_bulb = len(light)
        moments = 0
        rightmost_blue = 0  # also keeps track of number of blue
        for k in range (num_bulb):  # k keeps track of number of on
            bulb = abs(light[k])
            light[bulb-1] *= -1     # turn on bulb
            # update rightmost_blue
            while rightmost_blue < num_bulb and light[rightmost_blue] < 0:
                rightmost_blue += 1
            # update moments
            if rightmost_blue == k + 1: 
                moments += 1
            
        return moments



    # ----------------------------------------------------------------------------------
    # Leetcode 1227. Airplane Seat Assignment Probability
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5



    # ----------------------------------------------------------------------------------
    # Leetcode 1033. Moving Stones Until Consecutive
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        l = []
        ans = [-1] * 2
        l.append(a)
        l.append(b)
        l.append(c)
        l.sort();         

        ans[1] = l[2] - l[0] - 2

        if l[0] + 1 == l[1] and l[1] + 1 == l[2]:
            ans[0] = 0
        elif (l[0] + 1 == l[1] or l[1] + 1 == l[2]) or (l[0] + 2 == l[1] or l[1] + 2 == l[2]): 
            ans[0] = 1
        else:
            ans[0] = 2

        return ans




if __name__ == "__main__":
    leetcode = Solution()

    # -----------------  360  -----------------
    # nums = [-4, -2, 2, 4]
    # result = leetcode.sortTransformedArray(nums, 1,3,5)
    # print(result)

    # -----------------  12  -----------------
    # print(leetcode.intToRoman(1994))

    # -----------------  1154  -----------------
    # date = "2004-03-01"
    # print( leetcode.dayOfYear(date) )

    # -----------------  367  -----------------
    print( leetcode.isPerfectSquare(14) )










