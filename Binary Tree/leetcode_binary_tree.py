"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Tree  =========================================================
1. Leetcode 104. Maximum Depth of Binary Tree
2. Leetcode 226. Invert Binary Tree

"""


from typing import List

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # build tree: take an array
    def buildTree(self, data):
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















class Solution:
    # Leetcode 104. Maximum Depth of Binary Tree
    def maxDepth(self, root: Node) -> int:
        if not root: return 0

        def count(root, depth) -> int:
            # base case
            if not root:
                return depth

            # do recursion
            left_level = count(root.left, depth + 1)
            right_level = count(root.right, depth + 1)

            return max(left_level, right_level)

        return count(root, 0)

    
    # Leetcode 226. Invert Binary Tree
    def invertTree(self, root: Node) -> Node:
        if not root: 
            return None

        def postOrder(root):
            # Base case: when we reach leaf
            if not root:
                return 

            # DFS
            left = postOrder(root.left)
            right = postOrder(root.right)

            root.left = right
            root.right = left

            return root
        
        return postOrder(root)



















if __name__ == "__main__":
    leetcode = Solution()
    tree = Node()

    # ---------------------  104  ---------------------
    array = [3,9,20,None,None,15,7]
    root = tree.buildTree(array)
    print( "Max depth: ", leetcode.maxDepth(root) )


