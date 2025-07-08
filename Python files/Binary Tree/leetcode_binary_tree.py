"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Tree  =========================================================
(Easy)
1. Leetcode 104. Maximum Depth of Binary Tree
2. Leetcode 226. Invert Binary Tree
3. Leetcode 617. Merge Two Binary Trees
4. Leetcode 404. Sum of Left Leaves

(Medium)
5. Leetcode 1315. Sum of Nodes with Even-Valued Grandparent   
6. Leetcode 199. Binary Tree Right Side View
7. Leetcode 669. Trim a Binary Search Tree
================================================================
Kenny Talks Code: 
Problems involve path finding: given a tree, find a path that optimizes the sub criteria
8. Leetcode 112: Path Sum (Easy)
9. Leetcode 113: Path Sum II
10.Leetcode 129. Sum Root to Leaf Numbers
11.Leetcode 124. Binary Tree Maximum Path Sum (Hard)
12.Leetcode 543. Diameter of Binary Tree (Easy, but feels like Medium)
13.Leetcode 298: BT Longest Consucutive Sequence

Problems involve tree traversal: explore all nodes in the tree, usually in some unique ways other 
than pre-order, in-order and post-order
14.Leetcode 102. Binary Tree Level Order Traversal  
15.Leetcode 515. Find Largest Value in Each Tree Row
16.Leetcode 116. Populating Next Right Pointers in Each Node
17.Leetcode 117. Populating Next Right Pointers in Each Node II
18.Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal 
19.Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal
20.Leetcode 889. Construct Binary Tree from Preorder and Postorder Traversal

"""


from typing import List
from queue import Queue

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


    # --------------------------------------------------------------------
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
            # todo
            root.left = right
            root.right = left
            return root
        
        return postOrder(root)


    # --------------------------------------------------------------------
    # Leetcode 617. Merge Two Binary Trees
    def mergeTrees(self, root1: Node, root2: Node) -> Node:
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


    # --------------------------------------------------------------------
    # Leetcode 404. Sum of Left Leaves
    def sumOfLeftLeaves(self, root: Node) -> int:
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
    

    # ======================================================================================================
    # --------------------------------------------------------------------
    # Leetcode 1315. Sum of Nodes with Even-Valued Grandparent
    def sumEvenGrandparent(self, root: Node) -> int:
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


    # --------------------------------------------------------------------
    # Leetcode 199. Binary Tree Right Side View
    def rightSideView(self, root: Node) -> List[int]:
        level_order_traversal = self.levelOrder(root)
        right_side_view = []
        for level in level_order_traversal:
            right_side_view.append(level[-1])
        
        return right_side_view


    # --------------------------------------------------------------------
    # Leetcode 669. Trim a Binary Search Tree
    def trimBST(self, root: Node, low: int, high: int) -> Node:
        # helper function --------------------------------------------------
        def helper(root):
            # 1.Base case(s)
            if not root:
                return None
            
            # root in range
            if low <= root.val and root.val <= high:
                root.left = helper(root.left)
                root.right = helper(root.right)
            # 2+3 perform on root.left and root.right
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


    # ======================================================================================================
    # --------------------------------------------------------------------
    # Leetcode 112: Path Sum
    def hasPathSum(self, root: Node, targetSum: int) -> bool:
        # --------- helper function ---------
        def helper(root: Node, targetSum: int) -> bool:    
            # Step 1: Find one or more base case
            # Base case: Found a leaf
            if (not root.right) and (not root.left): 
                if targetSum == root.val: return True
                else: return False

            found = False
            # Step 2: Calling the same function on left subtree
            if root.left:
                found = found or helper(root.left, targetSum-root.val)
            
            # Step 3: Calling the same function on right subtree
            if root.right:
                found = found or helper(root.right, targetSum-root.val)

            # Step 4: Joining the result
            return found
        # ------------------------------------
        if not root: return False

        return helper(root, targetSum)
        
    
    # --------------------------------------------------------------------
    # Leetcode 113: Path Sum II
    # --------- helper function ---------
    def helper2(self, root_helper, targetSum_helper, curr_helper, res_helper):    
        # Step 1: Find one or more base case
        if not root_helper: return 
        else: curr_helper.append(root_helper.val)
        # Base case: Found a good leave
        if (not root_helper.right) and (not root_helper.left) and (targetSum_helper == root_helper.val):
            res_helper.append(list(curr_helper))

        # Step 2: Calling the same function on left subtree
        self.helper2(root_helper.left, targetSum_helper - root_helper.val, curr_helper, res_helper)
        # Step 3: Calling the same function on right subtree
        self.helper2(root_helper.right, targetSum_helper - root_helper.val, curr_helper, res_helper)
        # Step 4: Remove the root so it can explore the other path
        curr_helper.pop()
    # ------------------------------------

    def pathSum(self, root: Node, targetSum: int) -> List[List[int]]:
        res = []
        curr = []
        self.helper2(root, targetSum, curr, res)
        return res


    # --------------------------------------------------------------------
    # Leetcode 129. Sum Root to Leaf Numbers  
    def helper_129(self, root, current, result):
        # Step 1: Base case
        if not root: return

        current.append(root.val)
        # Step 2: When and How to build the solution
        if (not root.left) and (not root.right):
            result.append(list(current))

        # Step 3: Recursive calls
        self.helper_129(root.left, current, result)
        self.helper_129(root.right, current, result)

        # Step 4: Back track or return
        current.pop()       # explore other paths

    def sumNumbers(self, root: Node) -> int:
        all_numbers = list()
        current_path = list()
        self.helper_129(root, current_path, all_numbers)
        sum = 0
        for num in all_numbers:
            for i,val in enumerate(reversed(num)):
                sum += val * ( 10**i )

        return sum


    # --------------------------------------------------------------------
    # Leetcode 124. Binary Tree Maximum Path Sum
    # Notice: This problem doesn't have the Optimal Substructure Property. Meaning f(root) != max(f(root.left), f(root.right))
    def helper_124(self, root: Node) -> int:
        # Step 1: Base case(s)
        if not root: return 0

        # Step 2: Recursive call
        # Ignore the subtree that has a negative MPS
        left_MPS = max(0, self.helper_124(root.left) )
        right_MPS = max(0, self.helper_124(root.right) )

        # Step 3: Build the solution
        # At any given root node, we want to compute MPS that can be formed with the given nodes (root, left, right) since we can always traverse in in-order 
        max_MPS = root.val + left_MPS + right_MPS
        self.result_124 = max (self.result_124, max_MPS)

        # Step 4:
        # We can only return (left branch + root) or (right branch + root)
        return max(root.val + left_MPS, root.val + right_MPS)

    def maxPathSum(self, root: Node) -> int:
        if not root: return 0
        self.result_124 = float('-inf')
        self.helper_124(root)

        return self.result_124
    
    
    # --------------------------------------------------------------------
    # Leetcode 543. Diameter of Binary Tree
    def helper_543(self, root: Node) -> int:
        # Step 1: Base case(s)
        if not root:
            return 0  # depth of null node is 0

        # Step 2: Recursive call
        left_depth = self.helper_543(root.left)
        right_depth = self.helper_543(root.right)

        # Step 3: Build the solution
        # Diameter at this node = left depth + right depth
        local_diameter = left_depth + right_depth
        self.result_543 = max(self.result_543, local_diameter)

        # Step 4:
        # Return depth to parent = 1 + max depth of children
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Node) -> int:
        self.result_543 = 0
        self.helper_543(root)
        return self.result_543


    # --------------------------------------------------------------------
    # Leetcode 298: BT Longest Consecutive Sequence
    def helper_298(self, root) -> int:
        # Step 1: Base cases
        if not root:
            return 0
        if (not root.left) and (not root.right):
            return 1

        # Step 2: Recursive calls
        max_len_left = self.helper_298(root.left)
        max_len_right = self.helper_298(root.right)

        # Step 3: When and How to build the solution
        max_len = 1
        if root.left and root.val + 1 == root.left.val:
            max_len = max(max_len, 1 + max_len_left)
        if root.right and root.val + 1 == root.right.val:
            max_len = max(max_len, 1 + max_len_right)
        
        self.result_298 = max(self.result_298, max_len)
        # Step 4:
        return max_len
    
    def longestConsecutive(self, root: Node) -> int:
        if not root: return 0

        self.result_298 = 0
        answer = self.helper_298(root)

        return max( self.result_298, answer )



    # ======================================================================================================
    # --------------------------------------------------------------------
    # Leetcode 102. Binary Tree Level Order Traversal    
    def levelOrder(self, root: Node) -> List[List[int]]:
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


    # --------------------------------------------------------------------
    # Leetcode 515. Find Largest Value in Each Tree Row
    def helper_515(self, root, level, ans):
        # 1. Base case: 
        if not root: return 

        # 2. Build solution:
        if len(ans) == level:
            ans.append(float('-inf'))
        ans[level] = max(ans[level], root.val)

        # 3. Recursive call
        self.helper_515(root.left, level+1, ans)
        self.helper_515(root.right, level+1, ans)

        # 4. Return or back track - no need

    def largestValues(self, root: Node) -> List[int]:
        result = list()
        self.helper_515(root, 0, result)

        return result


    # --------------------------------------------------------------------
    # Leetcode 116. Populating Next Right Pointers in Each Node
    # This solution take O(1) extra space, and it resembles the Queue behavior
    def connect(self, root: Node) -> Node:
        if not root: return root

        firstNodeOnLevel = root     # This acts as an anchor so we can always retrive the first node of each level
        while firstNodeOnLevel:
            current = firstNodeOnLevel
            # Each of these while loops represent a level. If current is None, it means we have reach the last Node of this level
            while current:
                # We can do this because this is a perfect binary tree
                if current.left:
                    current.left.next = current.right
                # This means current is not the last Node on this level yet. If it is, then current.right.next is already correctly pointing to None
                if current.right and current.next:
                    current.right.next = current.next.left
                current = current.next
            
            # Move on to the next level. 
            firstNodeOnLevel = firstNodeOnLevel.left
        
        return root 
            

    # --------------------------------------------------------------------
    # Leetcode 117. Populating Next Right Pointers in Each Node II
    def connect_117(self, root: Node) -> Node:
        if not root: return 

        q = Queue()
        q.put(root)
        q.put(None)
        level = list()

        while not q.empty(): 
            pop = q.get()
            if pop:
                level.append(pop)
                if pop.left: q.put(pop.left)
                if pop.right: q.put(pop.right)
            else:   # reach None
                if not q.empty(): q.put(None)
                for i in range(len(level) - 1):
                    current = level[i]
                    current_next = level[i+1]
                    current.next = current_next
                level[len(level) - 1].next = None
                level.clear()
        
        return root


    # --------------------------------------------------------------------
    # Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal   
    # Pre-order: root->left->right => the root will always be the first element (preorder[0])
    # In-order: left->root->right => if we know the index of root in the inorder array, we can recursively split the entire array into two subtrees
    def buildTree_105(self, preorder: List[int], inorder: List[int]) -> Node:
        # ----------------------------------------------
        def arrayToTree_105(left: int, right: int) -> Node:
            # Step 1: Base case
            if left > right or self.preorderIndex >= len(preorder): 
                return None

            # Todo: construct a root
            rootValue = preorder[self.preorderIndex]
            root = Node( rootValue )
            inorderIndex = inorder_dict[ rootValue ]    # with inorderIndex, we can split the inorder array in two halves
            self.preorderIndex += 1                     # update for the next root

            # Step 2: Recursive call
            # Step 3: Build the solution 
            # Bottom-up
            root.left = arrayToTree_105(left, inorderIndex - 1)
            root.right = arrayToTree_105(inorderIndex + 1, right)
                
            return root
        # ----------------------------------------------
        inorder_dict = dict()           # store the index of each value in the inorder array
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        # start constructing each root at a time
        self.preorderIndex = 0

        return arrayToTree_105(0, len(preorder) - 1)


    # --------------------------------------------------------------------
    # Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal
    # Super similar to LC 105, only diff is that in post-order traversal, the root of the main tree will be in the end of the array
    # When we recursively construct the root.left and root.right, we have to put the root.right BEFORE root.left
    def buildTree_106(self, inorder: List[int], postorder: List[int]) -> Node:
        # ----------------------------------------------
        def arrayToTree_106(left: int, right: int) -> Node:     # left and right represent a range of inorder
            # Base case
            if left > right or self.postOrderIndex < 0: return None

            # Todo: construct a root
            root_value = postorder[self.postOrderIndex]
            root = Node( root_value )
            inorderIndex = inorder_dict[ root_value ]           # with inorderIndex, we can split the inorder array in two halves
            self.postOrderIndex -= 1                            # update for the next root

            # Step 2: Recursive call
            # Step 3: Build the solution 
            # Bottom-up
            root.right = arrayToTree_106(inorderIndex + 1, right)
            root.left = arrayToTree_106(left, inorderIndex - 1)
                
            return root
        # ----------------------------------------------
        inorder_dict = dict()           # store the index of each value in the inorder array
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        # start constructing each root at a time
        self.postOrderIndex = len(postorder) - 1

        return arrayToTree_106(0, len(postorder) - 1)


    # ------------------------- -------------------------------------------
    # Leetcode 889. Construct Binary Tree from Preorder and Postorder Traversal
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Node:
        # ----------------------------------------------
        def arrayToTree_889(left: int, right: int) -> Node:
            # Base case
            if self.preorderIndex_889 >= len(pre) or left > right: return None

            root_value = pre[self.preorderIndex_889]
            root = Node( root_value )
            
            self.preorderIndex_889 += 1 
            if left == right:               # meaning the .left of root does not exist
                return root

            potential_left = root_value     # in preOrder traversal, the value right next to it can be a potential .left

            postOrderIndex_potential_left = post_dict[potential_left]

            root.left = arrayToTree_889(left, postOrderIndex_potential_left)
            root.right = arrayToTree_889(postOrderIndex_potential_left + 1, right - 1)

            return root
        # ----------------------------------------------

        post_dict = dict()
        for ind, val in enumerate(post):
            post_dict[val] = ind
        
        self.preorderIndex_889 = 0

        return arrayToTree_889(0, len(pre) - 1)








# ====================================================================================================================
# ====================================================================================================================




if __name__ == "__main__":
    leetcode = Solution()
    tree = Node()

    # ---------------------  104  ---------------------
    # array = [3]
    # root = tree.buildTree(array)
    # print( "Max depth: ", leetcode.maxDepth(root) )

    # ---------------------  113  ---------------------
    # array = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    # root = tree.buildTree(array)
    # targetSum = 22
    # print( leetcode.pathSum(root, targetSum) )

    # ---------------------  129  ---------------------
    # array = [4,9,0,5,1]    
    # root = tree.buildTree(array)
    # print( leetcode.sumNumbers(root) )

    # ---------------------  129  ---------------------
    # array = [2,6, 3, 7, 100, 2, 4, 100, 100, 100, 100, 100, 100, 5, 100]
    # root = tree.buildTree(array)
    # print( leetcode.longestConsecutive(root) )

    # ---------------------  1315  ---------------------
    array = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
    root = tree.buildTree(array)
    print( "Sum: ", leetcode.sumEvenGrandparent(root) )