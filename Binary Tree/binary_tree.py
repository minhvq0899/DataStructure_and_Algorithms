"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Binary Tree =========================================================


"""

from typing import List

# Node for tree
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def __repr__(self):
        return str( self.val )


# build tree: take an array
def buildTree(data):
    n = len(data)
    
    if n == 0:
        return Node()

    root = Node(data[0])

    # helper function -------------------------------------------
    def insertNode(root, i, n):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < n:
            left_val = data[left_idx]
            left_node = Node( left_val )
            root.left = insertNode( left_node, left_idx, n )

        if right_idx < n:
            right_val = data[right_idx]
            right_node = Node( right_val )
            root.right = insertNode( right_node, right_idx, n )

        return root # back-tracking
    # ------------------------------------------------------------
    tree = insertNode(root, 0, n)
    return tree


# pre-order traversal
def preOrder(root):
    if not root:
        return 
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)



# Invert Binary Tree




if __name__ == "__main__":
    data = [1,2,3,4,5,6,7]
    tree = buildTree(data)

    preOrder(tree)











