# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return
        res = []
        count, bigg = 0, root.val
        def dfs(root, res, bigg):
            nonlocal count
            if not root:
                return
            res.append([root.val, bigg])
            if root.val >= bigg:
                bigg = root.val
                count += 1
            if not root.left and not root.right:
                bigg = res.pop()[-1]
            dfs(root.left, res, bigg)
            dfs(root.right, res, bigg)
        dfs(root, res, bigg)
        return count