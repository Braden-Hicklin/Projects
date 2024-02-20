# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        Min, Max = -2147483648, 2147483648
        return self.validateBST(root, Min, Max)

    def validateBST(self, root, Min, Max):
        if not root:
            return True
        
        if root.val < Min or root.val > Max:
            return False
        
        return (self.validateBST(root.left, Min, root.val - 1) and self.validateBST(root.right, root.val + 1, Max))