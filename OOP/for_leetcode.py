# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # base case 0: if root == None
        if root is None:
            return 0
        
        # base case 1: if node's value in range
        if low < root.val and root.val < high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        
        # base case 2: if node's val == low
        if low == root.val: 
            return root.val + self.rangeSumBST(root.right, low, high)
        
        # base case 3: if node's val == high
        if high == root.val: 
            return root.val + self.rangeSumBST(root.left, low, high)
        
        # base case 4: if node's val is less than low 
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
         
        # Base case 5: 
        if high < root.val:
            return self.rangeSumBST(root.left, low, high)


if __name__ == "__main__":
    leaf3 = TreeNode(3, None, None)
    leaf7 = TreeNode(7, None, None)
    leaf18 = TreeNode(18, None, None)
    leaf5 = TreeNode(5, leaf3, leaf7)
    leaf15 = TreeNode(15, None, leaf18)
    
    root = TreeNode(10, leaf5, leaf15)

    ans = Solution()
    print(ans.rangeSumBST(root, 7, 15))


