"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Tree  =========================================================
1. Leetcode 104. Maximum Depth of Binary Tree
2. Leetcode 226. Invert Binary Tree
3. Leetcode 617. Merge Two Binary Trees
4. Leetcode 1315. Sum of Nodes with Even-Valued Grandparent
5. Leetcode 102. Binary Tree Level Order Traversal    
6. Leetcode 199. Binary Tree Right Side View
6. Leetcode 404. Sum of Left Leaves
7. Leetcode 669. Trim a Binary Search Tree

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

    
    # Leetcode 617. Merge Two Binary Trees
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 1.Base cases
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        # 2+3.Calling the same fn on the left and right subtree
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1


    # Leetcode 1315. Sum of Nodes with Even-Valued Grandparent
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result_sum = 0
        
        # helper function -----------------------------------------------------
        def helper(root):
            if root.left:
                if root.val % 2 == 0:
                    if root.left.left: 
                        self.result_sum += root.left.left.val
                    if root.left.right: 
                        self.result_sum += root.left.right.val
                helper(root.left)
                
            if root.right:
                if root.val % 2 == 0:
                    if root.right.left: 
                        self.result_sum += root.right.left.val
                    if root.right.right: 
                        self.result_sum += root.right.right.val
                helper(root.right)
        # ---------------------------------------------------------------------
        helper(root)
        
        return self.result_sum


    # Leetcode 404. Sum of Left Leaves
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.leftSum = 0
        
        # ---------- helper function ----------
        def helper(root):
            # 1.Base case(s)
            if not root:
                return 0
            
            if root.left: # this means root is not leave
                if not root.left.left and not root.left.right: # root.left is leave
                    self.leftSum += root.left.val
                else:
                    helper(root.left)
            
            if root.right: 
                helper(root.right)
        # ---------------------------------------
            
        helper(root)
        
        return self.leftSum  


    # Leetcode 102. Binary Tree Level Order Traversal    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level_order_traversal = []
        if not root: return level_order_traversal
        
        q = Queue()
        
        # Step 1: enqueue root
        q.put(root)
        # Step 2: enqueue None (change level)
        q.put(None)
        
        level = []
        
        # Step 3: 
        while (not q.empty()):
            n = q.get()
            if n: # if n is not None
                level.append(n.val)
                if n.left:
                    q.put(n.left)
                if n.right:
                    q.put(n.right)
            else:
                level_order_traversal.append(level)
                level = []
                if (not q.empty()): q.put(None)
                
        return level_order_traversal
    

   # Leetcode 199. Binary Tree Right Side View
    def rightSideView(self, root: TreeNode) -> List[int]:
        level_order_traversal = self.levelOrder(root)
        right_side_view = []
        for level in level_order_traversal:
            right_side_view.append(level[-1])
        
        return right_side_view


    # Leetcode 669. Trim a Binary Search Tree
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # helper function --------------------------------------------------
        def helper(root):
            # 1.Base case(s)
            if not root:
                return None
            
            # 2+3. 
            if low <= root.val and root.val <= high:
                root.left = helper(root.left)
                root.right = helper(root.right)
            else:
                # Case 1
                if not root.left and not root.right:
                    return None
                # Case 2
                if root.val < low:
                    if root.right: 
                        return helper(root.right)
                    else:
                        return None
                # Case 3
                if root.val > high:
                    if root.left:
                        return helper(root.left)
                    else:
                        return None
                        
            # 4.Join
            return root
        # --------------------------------------------------------------------
        
        return helper(root)






# ====================================================================================================================
# ====================================================================================================================




if __name__ == "__main__":
    leetcode = Solution()
    tree = Node()

    # ---------------------  104  ---------------------
    array = [3,9,20,None,None,15,7]
    root = tree.buildTree(array)
    print( "Max depth: ", leetcode.maxDepth(root) )


