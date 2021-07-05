"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Binary Search Tree =========================================================
Class Node
Class BST
    addNode(root, val) -> root
    pre_oreder(root)
    search(root, val) -> node
    minValueNode(node) -> node
    deleteNode(root, val) -> root

"""

from typing import List

# Class Node
class Node: 
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return str(self.val)


# Class Binary Search Tree
class BST:
    # O(H) with H is the height of tree
    # Worst case: O(n)
    def addNode(self,root, val):
        # 1.Base case(s)
        if not root:
            return Node(val)

        # 2+3. Call the same function on both left and right
        if val > root.val:
            root.right = self.addNode(root.right, val)
        else:
            root.left = self.addNode(root.left, val)
        
        # 4.Join the result
        return root


    # O(n)
    def pre_oreder(self,root): 
        if not root: return 
        print(root.val) # Father
        self.pre_order(root.left)
        self.pre_order(root.right)

 
    # O(logn)
    def search(self,root, val):
        if not root: return 
        while (val != root.val):
            if val > root.val:
                root = root.right
            else:
                root = root.left
        return root


    # helper function for delete node
    # to find the smallest left child
    def minValueNode(self,node):
        current = node
        while (current.left):
            current = current.left
        return current

 
    # delete node function
    # O(H) 
    # height will depend on the shape of the tree
    def deleteNode(self,root, val):
        # Step 1.Base case
        if not root: return root

        # Step 2+3. Find the node we want to delete
        if val > root.val:
            root.right = self.deleteNode(root.right, val)
        elif val < root.val:
            root.left = self.deleteNode(root.left, val)
        else: # this is where we found the node we want to delete
            # case 1: this root has 1 or no child
            if not root.left: 
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            # case 2: this root has 2 children
            temp = self.minValueNode(root.right) # Find replacement
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val) # Delete the replacement

        # Step 4. Join
        return root