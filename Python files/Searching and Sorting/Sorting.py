"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================= Different Sorting Algorithms =========================================
Class Sorting_algorithms will have the following functions:

1. Insertion Sort
2. Merge Sort
3. 

"""
from typing import List
import math

# ------------------------------------------------------------------------------------------------------------------
# class Insertion Sort
class Insertion:
    # we first need a helper function to switch 2 elements
    def switch(self, a: List[int], i: int, j: int):
        a[i], a[j] = a[j], a[i]

    def insertion_sort(self, a: List[int]):
        n = len(a)
        for i in range (1, n):
            for j in range (i, 0, -1):
                if a[j-1] > a[j]:
                    self.switch(a, j-1, j)
                else: 
                    break





# ------------------------------------------------------------------------------------------------------------------
# class Merge Sort
class Merge:
    aux = []
    def merge(self, a: List[str], lo: int, mid: int, hi: int):
        self.aux = [None] * (hi - lo)
        i = lo
        j = mid
        N = hi
        for k in range (0, len(self.aux)):
            if i == mid: # run out of element in above halve
                self.aux[k] = a[j]
                j += 1
            elif j == hi: # run out of element in below halve
                self.aux[k] = a[i]
                i += 1
            elif a[i] <= a[j]: 
                self.aux[k] = a[i]
                i += 1
            else:
                self.aux[k] = a[j]
                j += 1
        
        # now just have to copy everything from aux into array a
        for k in range (0, len(self.aux)):
            a[lo + k] = self.aux[k]

    # helper function that does the whole thing
    def sort(self, a: List[str], lo: int, hi: int):
        N = hi - lo
        # base case
        if N <= 1: 
            return # this mean the array only has one or less number of element
        mid = lo + math.ceil(N/2)
        self.sort(a, lo, mid)
        self.sort(a, mid, hi)
        self.merge(a, lo, mid, hi)

    # actual call
    def merge_sort(self, a: List[str]):
        self.sort(a, 0, len(a))



class leetcode_exercises:
    # this is a helper function to help find the longest repeated substring
    # Given: Two strings string s and t.
    # Task: Find the longest substring that appears at the beginning of both strings.
    def longest_common_prefix(self, s: str, t: str):
        count = 0
        for char in range(min(len(s), len(t))):
            if s[char] != t[char]:
                return s[:char]
        return s[:min(len(s), len(t))]


    def leetcode1062_longest_repeated_substring(self, s: str):
        """
        • Given: Two strings s and t.
        • Task: Find the longest substring that appears at the beginning of both strings.

        1. Form a suffix array
        """
        suffix = []
        for i in range (len(s)):
            suffix.append(s[i:]) 

        Merge().merge_sort(suffix)
        # print(suffix)

        lrs_final = ''
        for k in range(len(suffix) - 1):
            temp_lrs = self.longest_common_prefix(suffix[k], suffix[k+1])
            if len(temp_lrs) > len(lrs_final):
                lrs_final = temp_lrs

        return lrs_final         

        

if __name__ == "__main__":
    # a = [7,8,5,2,4,6,3]
    a = ['c', 'e', 'a', 'g', 'b', 'd', 'f']
    test_string = 'aacaagtttacaagc'
    
    """
    # test for insertion
    insertion = Insertion()
    insertion.insertion_sort(a) 
    print(a)
    
    # test for merge sort
    merge_obj = Merge()
    merge_obj.merge_sort(a)
    print(a)
    """

    # test for leetcode exercise
    LRS = leetcode_exercises()
    lrs = LRS.leetcode1062_longest_repeated_substring(test_string)
    print(lrs)







