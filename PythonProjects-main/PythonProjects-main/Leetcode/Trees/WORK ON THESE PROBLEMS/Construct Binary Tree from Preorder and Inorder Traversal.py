# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder) # length of inorder list
        s = set()
        stack = []

        root = None
        pre = 0 # preorder iterator
        iot = 0 # inorder iterator

        # run while the pre iterator is less than the length of inorder list
        while pre < n:
            node = None

            while True:
                # create the first node using head of preorder list
                node = TreeNode(preorder[pre])
                
                # first pass, set the first node to the root node
                if(root == None):
                    root = node
                
                # if stack is not empty 
                if(len(stack) > 0):
                # if the front of stack is in the set, discard it, add the element as the right node, and
                # remove from stack
                    if(stack[-1] in s):
                        s.discard(stack[-1])
                        stack[-1].right = node
                        stack.pop()
                # if the front of the stack is not in the set, add the element as the left node
                    else:
                        stack[-1].left = node
                
                # add the node to the stack
                stack.append(node)

                # if the parent loop condition is met or the elements in both lists are the same
                # then the node has been finalized and the child loop breaks
                if pre >= n or preorder[pre] == inorder[iot]:
                    pre += 1
                    break
                
                # increment the preorder iterator
                pre += 1
            # set node back to None
            node = None

            # while the length of the stack is greater than 0, and the iterator for inorder
            # is less than the length of inorder, and the first element in the stack does not
            # have the same value as the current int in inorder
            while (len(stack) > 0 and iot < n and stack[-1].val == inorder[iot]):
                # set front of stack to the node, remove it from the stack, and increment inorder
                # iterator
                node = stack[-1]
                stack.pop()
                iot += 1
            # if the node doesn't equal None, add to set and stack
            if(node != None):
                s.add(node)
                stack.append(node)

        return root