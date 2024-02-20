# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution using BFS w/ queue
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            subli = []
            for i in range(length):
                currNode = queue.popleft()
                if currNode:
                    subli.append(currNode.val)
                    queue.append(currNode.left)
                    queue.append(currNode.right)
            if subli:
                res.append(subli)
                
        return res