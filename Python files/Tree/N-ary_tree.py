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


Class N-ary Tree
    init(root)
    delete_nodes_and_reattach(to_delete: set)
    compute_height()
    print_tree(root)

Class Leetcode

    (Hard)
    Leetcode 428. Serialize and Deserialize N-ary Tree (Premium + Hard)

"""

from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class N_ary_tree:
    def __init__(self, root: Node):
        self.root = root

    def delete_nodes_and_reattach(self, to_delete: set[int]) -> Node:
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
        if self.root.val in to_delete:
            dummy = Node(-1)  # Temporary dummy root
            dummy.children = [self.root]
            dfs(self.root, dummy)
            return dummy.children[0] if dummy.children else None
        else:
            return dfs(self.root, None)
        
    def compute_height(self) -> int:
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

        return dfs(self.root, 0)

    def print_tree(self, root: Node, level: int = 0) -> None:
        if not root:
            return

        indent = "  " * level  # Indentation based on tree depth
        print(f"{indent}- {root.val}")  # Print current node

        for child in root.children:
            self.print_tree(child, level + 1)  # Recurse into child





# Leetcode 428. Serialize and Deserialize N-ary Tree
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        result = self.dfsSerialize(root)

        print(result)
        return result

    def dfsSerialize(self, root: 'Node') -> str:
        # base case:
        if not root: 
            return 

        # prepare a string for all children
        serialized_children = ""
        for child in root.children:
            serialized_children += self.dfsSerialize(child)

        # The return string will varies, depending on whether if root has any children
        if root.children:
            return "[{} {}]".format(root.val, serialized_children)
        else:
            return "[{}]".format(root.val)
	
    def deserialize(self, data: str) -> 'Node':
        # Base case
        if not data: return None
        # prepare token
        tokens = self.tokenize(data)
        index = 0
        # print(tokens)
        # ------------------------------------------------------
        def parse() -> 'Node': 
            nonlocal index

            # We expect tokens[index] to be "["
            if index > len(data) or tokens[index] != "[":
                return None

            # Skip the "[" and read the root value
            index += 1
            value = int(tokens[index])
            root = Node(value)
            index += 1

            # prepare the children
            while index < len(data) and tokens[index] != "]":
                # Case 1: list of children
                if tokens[index] == "[":   
                    # Since we are calling parse() here, the index is updated inside this function already -> no need to update index
                    child = parse()
                    if child:
                        root.children.append(child)
                # Case 2: just one child
                else:
                    childNode = Node(tokens[index])
                    root.children.append(childNode)
                    index += 1

            index += 1          # Skip the "]"
            return root
        # ------------------------------------------------------

        return parse()

    def tokenize(self, data: str) -> List[str]:
        result = []
        index = 0

        # Skip all white space
        while index < len(data):
            char = data[index]
            if char == '[' or char == ']':
                result.append(char)
                index += 1
            elif char.isdigit():
                num = ""
                while data[index].isdigit() and index < len(data):
                    num += data[index]
                    index += 1
                result.append(num)
            elif char == " ":
                index += 1

        return result

    def print_tree(self, root: Node, level: int = 0) -> None:
        if not root:
            return

        indent = "  " * level  # Indentation based on tree depth
        print(f"{indent}- {root.val}")  # Print current node

        for child in root.children:
            self.print_tree(child, level + 1)  # Recurse into child
        
    





if __name__ == "__main__":
    """
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    root.children = [node2, node3]
    node3.children = [node4, node5]
    node5.children = [node6]

    tree = N_ary_tree(root)

    tree.print_tree(tree.root)
    print("Height: ", tree.compute_height())
    tree.delete_nodes_and_reattach({3})

    print("\n After deleting node 3: ")
    tree.print_tree(tree.root)
    print("Height: ", tree.compute_height())
    """

    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    root.children = [node3, node2, node4]
    node3.children = [node5, node6]

    codec = Codec()
    codec.print_tree(root)
    s = codec.serialize(root)
    rootDeserialized = codec.deserialize(s)
    codec.print_tree(rootDeserialized)







