"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Search Tree  =========================================================
# ----- Easy -----
1. Leetcode 938. Range Sum of BST
2. Leetcode 783. Minimum Distance Between BST Nodes
3. Leetcode 450. Delete Node in a BST -> refer to BST.py

# ----- Medium -----
4. Leetcode 653. Two Sum IV - Input is a BST
5. Leetcode 230. Kth Smallest Element in a BST
6. Leetcode 538. Convert BST to Greater Tree
7. Leetcode 1382. Balance a Binary Search Tree 

"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ Easy """
    # --------------------------------------------------------------------
    # Leetcode 783. Minimum Distance Between BST Nodes
    def minDiffInBST(self, root: TreeNode) -> int:
        in_order_tree = []
        def in_order(node, left, right):
            final = float('inf')
            if node:
                root_val = node.val
                return min(root_val - left, right - root_val, in_order(node.right, root_val, right), in_order(node.left, left, root_val))
            return final
                
        return in_order(root, -float('inf'), float('inf'))
    
    def minDiffInBST2(self, root: TreeNode) -> int:
        # helper fn to traverse in-order
        def inOrder(root, inOrderList):
            if not root: return 
            
            inOrder(root.left, inOrderList)
            inOrderList.append(root.val)
            inOrder(root.right, inOrderList)       

        # traverse in-order -> the result array will be sorted
        inOrderList = []
        inOrder(root, inOrderList)

        print("inOrderList: ", inOrderList)

        minDiff = float('inf')
        for i in range (1, len(inOrderList)):
            minDiff = min( minDiff, inOrderList[i] - inOrderList[i-1] )

        return minDiff

    # --------------------------------------------------------------------
    # Leetcode 938. Range Sum of BST
    def dfs_938(self, root: TreeNode, low: int, high: int) -> int:
        if not root: return 0

        if low <= root.val and root.val <= high:
            return root.val + self.dfs_938(root.left, low, high) + self.dfs_938(root.right, low, high)

        return self.dfs_938(root.left, low, high) + self.dfs_938(root.right, low, high)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0

        return self.dfs_938(root, low, high)

    """ Medium """
    # --------------------------------------------------------------------
    # Leetcode 653. Two Sum IV - Input is a BST
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # helper function -----------------------------------------------
        def inorder_traversal(root: TreeNode, nodes: List[int]):
            if not root: return 
            inorder_traversal(root.left, nodes)
            nodes.append(root.val)
            inorder_traversal(root.right, nodes)
        # ---------------------------------------------------------------
        nodes = []
        inorder_traversal(root, nodes) # O(n)
        
        # Now since this is a sorted array, just two pointers to find if there are two elements in the BST with the sum of target
        i = 0
        j = len(nodes) - 1
        while i < j:
            if nodes[i] + nodes[j] == k:
                return True
            elif nodes[i] + nodes[j] > k:
                j -= 1
            else:
                i += 1
            
        return False


    # --------------------------------------------------------------------
    # Leetcode 230. Kth Smallest Element in a BST
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # We will take advantage of the in-order traversal, 
        # but we will not traverse in-order-ly the whole way (because it will be O(n))
        # we will use a stack to only traverse until we find the kth smallest element
        stack = []
        
        while (True):
            while root:
                # Append all the way to the smallest element
                stack.append(root)
                root = root.left

            # Check the current smallest node
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            # Beatifully done
            # The whole right subtree of root is smaller than the next node in stack (stack[-1])
            # So we reset root to add the whole right subtree to stack first before processing the next node in stack
            root = root.right


    # --------------------------------------------------------------------
    # Leetcode 538. Convert BST to Greater Tree
    def convertBST(self, root: TreeNode) -> TreeNode:
        returned_root = root
        stack = []
        prev_sum = 0
        
        # while the stack is not empty
        while stack or root is not None:
            while root:
                # push all the way to the largest element
                stack.append(root)
                root = root.right
            
            # Modify the value of each node
            root = stack.pop()
            root.val += prev_sum
            prev_sum = root.val
            
            # keep looking for largest element
            root = root.left
        
        return returned_root


    # --------------------------------------------------------------------
    # Leetcode 1382. Balance a Binary Search Tree
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Convert the tree to a sorted array using an in-order traversal O(n)
        sorted_tree = []
        # -------------------------------------------
        def inorderTraversal(root, sorted_tree):
            #base
            if not root:
                return 
            
            inorderTraversal(root.left, sorted_tree)
            sorted_tree.append(root.val)
            inorderTraversal(root.right, sorted_tree)
        # -------------------------------------------
            
        inorderTraversal(root, sorted_tree)
        
        # Step 2: Construct a new balanced tree from the sorted array recursively O(n)        
        # -------------------------------------------
        def buildTree(node_list):
            #base: if list is empty
            if len(node_list) == 0:
                return None
            
            #2+3
            mid = len(node_list) // 2
            root = TreeNode(node_list[mid])
            left_side = node_list[:mid]
            right_side = node_list[mid+1:]
            #recursion
            root.left = buildTree(left_side)
            root.right = buildTree(right_side)
            
            return root
        # -------------------------------------------
        
        root = buildTree(sorted_tree)
        return root




# =======================================================================================================================

if __name__ == "__main__":
    leetcode = Solution()

    # -----------------------------------------
    







