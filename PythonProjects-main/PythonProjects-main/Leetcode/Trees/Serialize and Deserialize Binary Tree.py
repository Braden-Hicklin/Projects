# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        q = collections.deque()
        q.append(root)
        level = []

        while q:
            t = q.pop()
            if not t:
                level.append('/')
            else:
                level.append(str(t.val))
                q.append(t.right)
                q.append(t.left)
        level = ','.join(level)
        return level
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        global t
        t = 0
        li = data.split(",")
        return self.construct(li)
    
    def construct(self, li):
        global t

        if li[t] == '/':
            return None
        root = TreeNode(int(li[t]))
        t += 1
        root.left = self.construct(li)
        t += 1
        root.right = self.construct(li)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))