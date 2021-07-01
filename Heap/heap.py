"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Heap =========================================================

Implementation of Heap
1. heapify/ buildHeap
2. insert
3. delete

"""

from typing import List

class MinHeap():
    # build a heap from an array
    def heapify(self, tree: List[int], n: int, i: int): # n is the length of tree
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2 

        if l < n and tree[l] < tree[smallest]:
            smallest = l
        
        if r < n and tree[r] < tree[smallest]:
            smallest = r

        if smallest != i:
            # switch only when we have to
            tree[i], tree[smallest] = tree[smallest], tree[i]
            # recursion
            self.heapify(tree, n, smallest)        

    # O(n)
    def buildHeap(self, tree: List[int], n: int):
        startIdx = n // 2 - 1
        for i in range (startIdx, -1, -1):
            self.heapify(tree, n, i)


    # insert an element into heap - O(log(N))
    def insert(self, tree: List[int], val: int): 
        '''
        Step 1: Insert that element in the end of the heap (last index in an array)
        Step 2: Swim that element up 
                While loop. If that element is smaller than it's parent -> switch
        '''
        tree.append(val) # step 1
        valIdx = len(tree) - 1 # index of tree

        # step 2: swim it up
        while valIdx >= 1 and tree[valIdx] < tree[ (valIdx - 1) // 2 ]:
            tree[valIdx], tree[ (valIdx - 1) // 2 ] = tree[ (valIdx - 1) // 2 ], tree[valIdx]
            valIdx = (valIdx - 1) // 2 


    # delete an element from heap - O(log(N))
    def delete(self, tree: List[int], idx: int):
        '''
        Step 1: Replace that element you want to delete with the last element in the heap
        Step 2: Heapify the tree at tree[0]
        Step 3: Delete that last element
        '''
        # step 1
        tree[idx] = tree[len(tree) - 1]
        # step 2
        self.heapify(tree, len(tree), 0)
        # step 3
        tree.pop()


if __name__ == "__main__":
    tree = [10, 7, 6, 1, 4, 3, 9, 0, 15]

    my_heap = MinHeap()
    my_heap.buildHeap(tree, len(tree))

    print(tree) # [0, 1, 3, 7, 4, 6, 9, 10, 15]

    my_heap.insert(tree, 8) # insert VALUE 8
    print("After inserting 8, we have: ", tree)

    my_heap.delete(tree, 8) # delete element at INDEX 8
    print("After deleting the element at index 8, we have: ", tree)

 