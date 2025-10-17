"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

=========================================================  Binary Tree  =========================================================
(Easy)
Leetcode 104. Maximum Depth of Binary Tree
Leetcode 226. Invert Binary Tree
Leetcode 617. Merge Two Binary Trees
Leetcode 404. Sum of Left Leaves

(Medium)
Leetcode 1315. Sum of Nodes with Even-Valued Grandparent   
Leetcode 199. Binary Tree Right Side View
Leetcode 669. Trim a Binary Search Tree
Leetcode 98. Validate Binary Search Tree
Leetcode 2265. Count Nodes Equal to Average of Subtree

================================================================
** Kenny Talks Code: 
** Problems involve path finding: given a tree, find a path that optimizes the sub criteria
Leetcode 112: Path Sum (Easy)
Leetcode 113: Path Sum II
Leetcode 129. Sum Root to Leaf Numbers
Leetcode 124. Binary Tree Maximum Path Sum (Hard)
Leetcode 543. Diameter of Binary Tree (Easy, but feels like Medium)
Leetcode 298: BT Longest Consucutive Sequence

** Problems involve tree traversal: explore all nodes in the tree, usually in some unique ways other 
than pre-order, in-order and post-order
Leetcode 102. Binary Tree Level Order Traversal  
Leetcode 662. Maximum Width of Binary Tree
Leetcode 515. Find Largest Value in Each Tree Row
Leetcode 116. Populating Next Right Pointers in Each Node
Leetcode 117. Populating Next Right Pointers in Each Node II
Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal 
Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal
Leetcode 889. Construct Binary Tree from Preorder and Postorder Traversal
Leetcode 103. Binary Tree Zigzag Level Order Traversal
Leetcode 314. Binary Tree Vertical Order Traversal
Leetcode 987. Vertical Order Traversal of a Binary Tree (Hard verion of 314)
Leetcode 863. All Nodes Distance K in Binary Tree

** Lowest Common Ancestor: https://www.geeksforgeeks.org/dsa/lowest-common-ancestor-binary-tree-set-1/
Leetcode 235. Lowest Common Ancestor of a Binary Search Tree
Leetcode 236. Lowest Common Ancestor of a Binary Tree
Leetcode 1644. Lowest Common Ancestor of a Binary Tree II
Leetcode 1650. Lowest Common Ancestor of a Binary Tree III
Leetcode 1676. Lowest Common Ancestor of a Binary Tree IV
Leetcode 1123. Lowest Common Ancestor of Deepest Leaves
Leetcode 865. Smallest Subtree with all the Deepest Nodes - exactly the same as 1123
Leetcode 2096. Step-By-Step Directions From a Binary Tree Node to Another


(Hard)
Leetcode 297. Serialize and Deserialize Binary Tree
"""


from typing import List
from queue import Queue
from collections import deque, defaultdict
import Optional
import math


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




"""
(Easy)
"""
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
    """
    (Medium)
    """
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

    # --------------------------------------------------------------------
    # Leetcode 98. Validate Binary Search Tree
    # https://www.geeksforgeeks.org/dsa/a-program-to-check-if-a-binary-tree-is-bst-or-not/#
    # The idea is to use inorder traversal of a binary search tree, in which the output values are sorted in ascending order.
    # We can avoid the use of an Auxiliary Array. While doing In-Order traversal, we can keep track of previously visited value. 
    # If the value of the currently visited node is less than the previous value, then the tree is not BST.
    def isValidBST(self, root: 'TreeNode') -> bool:
        # nodeValues = []
        nodeValue = float('-inf')
        validBST = True

        # -----------------
        def inorder(root):
            nonlocal nodeValue, validBST

            # Base case:
            if not root:
                return 
            
            inorder(root.left)
            # nodeValues.append(root.val)
            if root.val <= nodeValue:
                validBST = False
            nodeValue = root.val
            inorder(root.right)
        # -----------------

        inorder(root)
        # print(nodeValues)
        # for i in range(1, len(nodeValues)):
        #     if nodeValues[i] <= nodeValues[i-1]:
        #         return False

        return validBST


    # --------------------------------------------------------------------
    # Leetcode 2265. Count Nodes Equal to Average of Subtree
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0
        # -----------------------------------
        # Given a node, return [the sum of the subtree of root, # of node in that subtree]
        def dfs(root) -> List[int]:
            nonlocal result

            # 1. base case
            if not root:
                return [0,0]
            
            # 2. dfs part
            left_sum, left_number_nodes = dfs(root.left)
            right_sum, right_number_nodes = dfs(root.right)

            # 3. action
            subtree_sum = (root.val + left_sum + right_sum)
            subtree_total_node = (1 + left_number_nodes + right_number_nodes)
            if math.floor(subtree_sum / subtree_total_node) == root.val:
                result += 1

            return [subtree_sum, subtree_total_node]
        # -----------------------------------
        dfs(root)

        return result

    # ======================================================================================================
    """
    Problems involve path finding: given a tree, find a path that optimizes the sub criteria
    """
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
    """
    Problems involve tree traversal: explore all nodes in the tree, usually in some unique ways other 
    """
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
    # Leetcode 662. Maximum Width of Binary Tree
    # If index of parent is n, the index of left child is (2n), and right child is (2n+1)
    def widthOfBinaryTree(self, root: 'TreeNode') -> int:
        dq = deque([(root, 1)])
        # dq.append("Change level")     # Traverse layer by layer, do no need signal to change level
        maxWidth = 0

        while dq:
            levelLen = len(dq)
            firstNode, firstLevelIndex = dq[0]      # First node of the level
            lastNode, lastLevelIndex = dq[-1]       # Last node of the level

            # Compute level width
            levelWidth = lastLevelIndex - firstLevelIndex + 1
            maxWidth = max(maxWidth, levelWidth)

            # Add all node in the next layer in the deque
            for _ in range(levelLen):
                node, index = dq.popleft()
                if node.left:
                    dq.append((node.left, index*2))
                if node.right:
                    dq.append((node.right, index*2+1))

        return maxWidth


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


    # ---------------------------------------------------------------------
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

    
    # ---------------------------------------------------------------------
    # Leetcode 103. Binary Tree Zigzag Level Order Traversal
    def zigzagLevelOrder(self, root: 'TreeNode') -> List[List[int]]:
        if not root:
            return []
            
        dq = deque([root])
        zigzagOrder = []
        levelCount = 1

        while dq:
            # Process each level
            level = []
            for _ in range(len(dq)):
                pop = dq.popleft()
                level.append(pop.val)
                # Left -> Right
                if levelCount % 2 == 1:
                    if pop.left:
                        dq.append(pop.left)
                    if pop.right:
                        dq.append(pop.right)
                # Right -> Left
                else:
                    if pop.right:
                        dq.append(pop.right)
                    if pop.left:
                        dq.append(pop.left)

            zigzagOrder.append(level)
            dq.reverse()
            levelCount += 1

        return zigzagOrder


    # --------------------------------------------------------------------
    # Leetcode 314. Binary Tree Vertical Order Traversal
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        columnIndexes = defaultdict(list)
        # -------------------------------------
        def bfs(root: TreeNode):
            dq = deque([(root, 0)])

            while dq:
                node, column = dq.popleft()
                columnIndexes[column].append(node.val)
                
                # process child from left -> right
                if node.left:
                    dq.append((node.left, column-1))
                if node.right:
                    dq.append((node.right, column+1))
        # -------------------------------------
        bfs(root)
        # print(columnIndexes)

        minColumnIndex = min(columnIndexes)
        maxColumnIndex = max(columnIndexes)
        result = []
        for i in range(minColumnIndex, maxColumnIndex+1):
            result.append(columnIndexes[i])

        return result

    # --------------------------------------------------------------------
    # Leetcode 987. Vertical Order Traversal of a Binary Tree (Hard verion of 314)
    # For this problem, we can optimize like this: store all tuple (col, row, node.val) in a list. After traversing BFS, sort this list
    # --> all tuples will be sorted by col, then row, then node value, just like we want
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        coordinateToNodeValueMap = defaultdict(list)            # One coordinate can have multiple node values. (row, col) -> [v1, v2, etc]
        columnToRowsMap = defaultdict(set)                      # For each col, store all rows that exists a coordinate in our tree
        # -------------------------------------
        def bfs(root: TreeNode):
            dq = deque([(root, (0,0))])

            while dq:
                node, coordinate = dq.popleft()
                row, col = coordinate
                coordinateToNodeValueMap[coordinate].append(node.val)
                columnToRowsMap[col].add(row)
                
                # process child from left -> right
                if node.left:
                    dq.append((node.left, (row+1, col-1)))
                if node.right:
                    dq.append((node.right, (row+1, col+1)))
        # -------------------------------------
        bfs(root)
        print(coordinateToNodeValueMap)
        print(columnToRowsMap)

        result = []
        minCol = min(columnToRowsMap)
        maxCol = max(columnToRowsMap)
        for col in range(minCol, maxCol+1):
            oneCol = []     # Store all values that have this col index
            for row in sorted(columnToRowsMap[col]):
                oneCordinateValues = coordinateToNodeValueMap[(row, col)]       # All the values in a coordinate
                if len(oneCordinateValues) > 1:
                    oneCordinateValues.sort()

                oneCol.extend(oneCordinateValues)

            result.append(oneCol)

        return result

    # --------------------------------------------------------------------
    # Leetcode 863. All Nodes Distance K in Binary Tree
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # A dict to store each node's parent
        # IMPORTANT: this needs to be a regular dict in Python instead of DefaultDict because
        # If pop.val is not in 'parents', parents[pop.val] will silently create a dummy TreeNode.
        # Later in BFS, you’ll try to access .val on this dummy node, which is not part of the real tree.
        # This can lead to infinite loops, incorrect results, or subtle bugs.
        parents = {}

        # BFS to populate our parents dict
        dq = deque([root])
        while dq:
            pop = dq.popleft()

            # Populate parents and queue
            if pop.left:
                dq.append(pop.left)
                parents[pop.left.val] = pop
            if pop.right:
                dq.append(pop.right)                
                parents[pop.right.val] = pop
        
        # BFS from target node to find all nodes distance K from target
        result = []
        dq = deque([target])
        visited = set()
        visited.add(target.val)
        layer = 0
        while dq:
            if layer == k:
                for _ in range(len(dq)):
                    pop = dq.popleft()
                    result.append(pop.val)
                break

            for _ in range(len(dq)):
                pop = dq.popleft()

                parent = parents[pop.val] if pop.val in parents else None
                for node in [pop.left, pop.right, parent]:
                    if node and node.val not in visited:
                        dq.append(node)
                        visited.add(node.val)

            layer += 1

        return result



    # ======================================================================================================
    """
    LCA
    """
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    # Leetcode 235. Lowest Common Ancestor of a Binary Search Tree
    # Doesn't require recursion - we can leverage the property of the BST
    # You walk down the tree from the root. As soon as p and q diverge (one on each side), you've found the LCA
    def lowestCommonAncestor235(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:       # Found LCA
                return root


    # This approach assumes that both the keys are present in the given tree
    # Leetcode 236. Lowest Common Ancestor of a Binary Tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Step 1: Base case
        if not root:
            return None
        
        # Return early: If root is either p or q, root is our LCA
        if root.val == p.val or root.val == q.val:
            return root
        
        # Step 3: Call recursive fn on both left and right subtree
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        # Step 4: Return
        # Case 4.1: If each node is on a different subtree -> LCA will be root
        if leftLCA and rightLCA:
            return root
        
        # Case 4.2
        return leftLCA if leftLCA != None else rightLCA


    # Leetcode 1644. Lowest Common Ancestor of a Binary Tree II
    # It performs a post-order traversal, checking both subtrees before deciding.
    # It tracks whether p and q were found during traversal.
    # It only returns the LCA if both nodes are present.
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ---------------------------------------
        def findLcaAndCheckExistance(root: 'TreeNode') -> tuple['TreeNode', bool, bool]:
            # Step 1: Base case
            if not root:
                return (None, False, False)
            
            # Step 3: Call recursive fn on both left and right subtree
            (leftLCACandidate, leftFoundP, leftFoundQ) = findLcaAndCheckExistance(root.left)
            (rightLCACandidate, rightFoundP, rightFoundQ) = findLcaAndCheckExistance(root.right)

            # Step 2: Check existance
            pExistance = leftFoundP or rightFoundP or p.val == root.val
            qExistance = leftFoundQ or rightFoundQ or q.val == root.val

            # Step 4: Return
            # Case 4.1: If current root is p or q
            if p.val == root.val or q.val == root.val:
                return (root, pExistance, qExistance)
            # Case 4.2: If both sides return non-null, then our LCA is root
            if leftLCACandidate and rightLCACandidate:
                return (root, pExistance, qExistance)
            # Case 4.3: Our LCA is just a candidate
            lcaCandidate = leftLCACandidate if leftLCACandidate != None else rightLCACandidate
            return (lcaCandidate, pExistance, qExistance)
        # ---------------------------------------
        candidateLCA, found_p, found_q = findLcaAndCheckExistance(root)

        return candidateLCA if found_p and found_q else None


    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.parent = None

    # Leetcode 1650. Lowest Common Ancestor of a Binary Tree III
    # Root of the tree is not passed into the function. You are only passed 'p' and 'q'
    def lowestCommonAncestor3(self, p: 'Node', q: 'Node') -> 'Node':
        pToRootSet = set()

        # Store all nodes from p to root in a set
        current = p
        while current:
            pToRootSet.add(current.val)
            current = current.parent

        # The first node in path q->root that exists in the set is our LCA
        current = q
        while current:
            if current.val in pToRootSet:
                return current
            else:
                current = current.parent

        return None


    # Leetcode 1676. Lowest Common Ancestor of a Binary Tree IV
    def lowestCommonAncestor4(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        targetSet = set()
        for node in nodes:
            targetSet.add(node.val)

        # -----------------------------------------------
        def lca(root) -> 'TreeNode':
            # Step 1: Base case
            if not root:
                return None
            
            # Return early: If root is in the set, root is our LCA
            if root.val in targetSet:
                return root
            
            # Step 3: Call recursive fn on both left and right subtree
            leftLCA = lca(root.left)
            rightLCA = lca(root.right)

            # Step 4: Return
            # Case 4.1: If each node is on a different subtree -> LCA will be root
            if leftLCA and rightLCA:
                return root
            
            # Case 4.2
            return leftLCA if leftLCA != None else rightLCA
        # -----------------------------------------------

        return lca(root)
        
    
    # Leetcode 1123. Lowest Common Ancestor of Deepest Leaves
    def lcaDeepestLeaves(self, root: 'TreeNode') -> 'TreeNode':
        # ---------------------------------------------------------
        # Return a potential LCA and the depth of this subtree
        # We will compute the depth of the tree bottom-up
        def lca(root) -> tuple[TreeNode, int]:
            # Step 1: base case
            if not root:
                return (None, 0)

            # Step 3: recursive calls
            (leftLca, leftDepth) = lca(root.left)
            (rightLca, rightDepth) = lca(root.right)

            # Step 4: return
            # 4.1: If left and right depths are equal → current node is LCA of deepest leaves
            if leftDepth == rightDepth:
                return (root, leftDepth+1)
            # 4.2 If one side is deeper → propagate that side’s result upward
            if leftDepth > rightDepth:
                return (leftLca, leftDepth+1)
            if leftDepth < rightDepth:
                return (rightLca, rightDepth+1)
        
        # ---------------------------------------------------------

        lca, _ = lca(root)
        return lca


    # Leetcode 2096. Step-By-Step Directions From a Binary Tree Node to Another
    # Solution 1: This problem can be solve by finding the LCA for 'start' and 'end' node, then constructing the path 
    # 'start'->LCA and LCA->'end' 
    # Solution 2: However, the solution below will convert the BT to a undirected graph, then run BFS on the graph
    def getDirections(self, root: 'TreeNode', startValue: int, destValue: int) -> str:
        graph = defaultdict(list)               # node value -> [parent value, left value, right value]
        # ------------------------------------------------------
        # Traverse the graph, with queue containing the node instead of node value
        def treeTraverseBFS(root: TreeNode):
            dq = deque([root])

            while dq:
                pop = dq.popleft()
                if not graph[pop.val]:
                    graph[pop.val] = [None, None, None]

                if pop.left:
                    graph[pop.val][1] = pop.left.val                    # Add pop.left
                    if not graph[pop.left.val]:
                        graph[pop.left.val] = [None, None, None]
                    graph[pop.left.val][0] = pop.val
                    dq.append(pop.left)
                
                if pop.right:
                    graph[pop.val][2] = pop.right.val                   # Add pop.right
                    if not graph[pop.right.val]:
                        graph[pop.right.val] = [None, None, None]
                    graph[pop.right.val][0] = pop.val
                    dq.append(pop.right)        
        # ------------------------------------------------------
        
        # Step 1: Traverse the tree once to collect parents and construct graph representation
        treeTraverseBFS(root)
        # print("graph: ", graph)

        # Step 2: BFS to construct the shortest path
        paths = defaultdict(int)
        visited = set()
        # ------------------------------------------------------
        # Traverse the graph, with queue containing the node value instead of node
        def bfs(start):
            dq = deque([start])

            while dq: 
                popValue = dq.popleft()
                visited.add(popValue)

                for neighborValue in graph[popValue]:
                    if neighborValue not in visited:
                        visited.add(neighborValue)
                        paths[neighborValue] = popValue
                        dq.append(neighborValue)                   
        # ------------------------------------------------------
        bfs(start = startValue)
        # print("paths: ", paths)

        # Step 3.1: Construct the value path
        current = destValue
        pathList = [destValue]
        while current != startValue:
            pathList.append(paths[current])
            current = paths[current]

        pathList.reverse()
        # print(pathList)

        # Step 3.2: Construct the letter path
        result = ""
        for i in range(len(pathList)-1):
            currentValue = pathList[i]
            nextValue = pathList[i+1]
            # Parent
            if nextValue == graph[currentValue][0]:
                result += 'U'
            # Left
            elif nextValue == graph[currentValue][1]:
                result += 'L'
            # Right
            elif nextValue == graph[currentValue][2]:
                result += 'R'

        return result
     

# ====================================================================================================================
# ====================================================================================================================


"""
(Hard)
"""
# --------------------------------------------------------------------
# Leetcode 297. Serialize and Deserialize Binary Tree
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string using bracketed DFS format."""
        result = self.dfs(root)
        print(result)

        return result 

    def dfs(self, root) -> str:
        if not root:
            return "[None]"

        left_serialized = self.dfs(root.left)
        right_serialized = self.dfs(root.right)

        return f"[{root.val} {left_serialized} {right_serialized}]"

    def deserialize(self, data):
        """Decodes the bracketed string back into a binary tree."""
        tokens = self.tokenize(data)
        print(tokens)
        index = 0
        # -----------------------------------------------------------------
        def parse():
            nonlocal index
            if index >= len(tokens) or tokens[index] != "[":
                return None

            index += 1  # Skip '['

            val = tokens[index]
            index += 1

            if val == "None":
                # Skip to closing bracket
                while index < len(tokens) and tokens[index] != "]":
                    index += 1
                index += 1  # Skip ']'
                return None

            node = TreeNode(int(val))
            node.left = parse()
            node.right = parse()

            index += 1  # Skip ']'
            return node
        # ----------------------------------------------------------------------

        return parse()

    def tokenize(self, data) -> list:
        """Splits the serialized string into meaningful tokens."""
        tokens = []
        i = 0
        while i < len(data):
            if data[i] in "[]":
                tokens.append(data[i])
                i += 1
            elif data[i].isspace():
                i += 1
            else:
                token = ""
                while i < len(data) and (data[i].isalnum() or data[i] == "-"):
                    token += data[i]
                    i += 1
                tokens.append(token)
        return tokens

    def print_tree(self, root: TreeNode, level: int = 0):
        """Pretty-prints the tree structure."""
        indent = "  " * level
        if not root:
            print(f"{indent}- None")
            return
        print(f"{indent}- {root.val}")
        self.print_tree(root.left, level + 1)
        self.print_tree(root.right, level + 1)
    

























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
    # array = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
    # root = tree.buildTree(array)
    # print( "Sum: ", leetcode.sumEvenGrandparent(root) )

    # ---------------------  297  ---------------------
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    root.left = node2
    root.right = node3
    node3.left = node4
    node3.right = node5
    node2.right = node6

    codec = Codec()
    codec.print_tree(root)
    s = codec.serialize(root)
    rootDeserialized = codec.deserialize(s)
    codec.print_tree(rootDeserialized)