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
    def merge(self, a: List[int], lo: int, mid: int, hi: int):
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
    def sort(self, a: List[int], lo: int, hi: int):
        N = hi - lo
        # base case
        if N <= 1: 
            print("return")
            return # this mean the array only has one or less number of element
        mid = lo + math.ceil(N/2)
        print(mid)
        self.sort(a, lo, mid)
        self.sort(a, mid, hi)
        self.merge(a, lo, mid, hi)

    # actual call
    def merge_sort(self, a: List[int]):
        self.sort(a, 0, len(a))

if __name__ == "__main__":
    a = [7,8,5,2,4,6,3]
    
    """
    # test for insertion
    insertion = Insertion()
    insertion.insertion_sort(a) 
    print(a)
    """

    # test for merge sort
    merge_obj = Merge()
    merge_obj.merge_sort(a)
    print(a)







