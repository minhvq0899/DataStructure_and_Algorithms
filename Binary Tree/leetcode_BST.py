"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Search Tree  =========================================================


"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        in_order_tree = []
        def in_order(node, left, right):
            final = float('inf')
            if node:
                root_val = node.val
                return min(root_val - left, right - root_val, in_order(node.right, root_val, right), in_order(node.left, left, root_val))
            return final
                
        return in_order(root, -float('inf'), float(inf))






if __name__ == "__main__":
    leetcode = Solution()

    # -----------------------------------------
    







