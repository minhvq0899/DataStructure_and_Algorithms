"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Math  =========================================================
1. Leetcode 360: Sort Transformed Array

"""


from typing import List


# Leetcode exercises
class Solution:
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





if __name__ == "__main__":
    leetcode = Solution()

    # -----------------  360  -----------------
    nums = [-4, -2, 2, 4]
    result = leetcode.sortTransformedArray(nums, 1,3,5)
    print(result)












