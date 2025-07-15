"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Binary Tree =========================================================

    1
   / \
  2   3
     / \
    4   5
        |
        6    

"""

from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def delete_nodes_and_reattach(root: Node, to_delete: set[int]) -> Node:
    # --------------------------------------------------
    def dfs(node: Node, parent: Node) -> Node:
        if not node:
            return None

        # dfs part
        # Process children first (post-order)
        new_children = []
        for child in node.children:
            updated_child = dfs(child, node)
            if updated_child:
                new_children.append(updated_child)

        node.children = new_children  # Update children after pruning

        # Todo
        if node.val in to_delete:
            # Reattach this node's children to its parent
            if parent:
                parent.children.extend(node.children)
            return None  # This node is deleted
        else:
            return node  # Keep this node
    # --------------------------------------------------

    # Special case: if root is deleted, we need to promote its children
    if root.val in to_delete:
        dummy = Node(-1)  # Temporary dummy root
        dummy.children = [root]
        dfs(root, dummy)
        return dummy.children[0] if dummy.children else None
    else:
        return dfs(root, None)
    


def compute_height(root: Node) -> int:
    # -------------------------------------------
    def dfs(root: Node, level = 0) -> int:
        # base case
        if not root: return 0

        # dfs 
        maxHeight = 0
        for child in root.children:
            maxHeight = max(maxHeight, dfs(child))

        return 1 + maxHeight
    # -------------------------------------------

    return dfs(root, 0)


def print_tree(root: Node, level: int = 0) -> None:
    if not root:
        return

    indent = "  " * level  # Indentation based on tree depth
    print(f"{indent}- {root.val}")  # Print current node

    for child in root.children:
        print_tree(child, level + 1)  # Recurse into child









if __name__ == "__main__":
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    root.children = [node2, node3]
    node3.children = [node4, node5]
    node5.children = [node6]

    print_tree(root)
    print("Height: ", compute_height(root))
    delete_nodes_and_reattach(root, {3})

    print("\n After deleting node 3: ")
    print_tree(root)
    print("Height: ", compute_height(root))









