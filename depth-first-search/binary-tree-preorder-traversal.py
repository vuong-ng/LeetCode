# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #iterative
        """
        stack, res = [],[]
        while stack or root:
            if not root:
                root=stack.pop()
                root= root.right
            elif root:
                stack.append(root)
                res.append(root.val)
                root=root.left
        return res
        """
        
        #recursive
        """
        ans = []
        def traverse(node):
            if not node:
                return
            ans.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ans
        """
        #iterative optimized
        stack, res =[], []
        if not root:
            return res
        stack.append(root)
        while stack:
            item = stack.pop()
            if item:
                res.append(item.val)
                stack.append(item.right)
                stack.append(item.left)
        return res



            

        
