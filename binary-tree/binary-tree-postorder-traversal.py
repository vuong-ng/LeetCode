# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #recursive
        """
        ans = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            ans.append(root.val)
        traverse(root)
        return ans
        """

        #iterative
        '''
        if not root:
            return []
            
        stack, res = [root,],[]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left: stack.append(root.left)
            if root.right: stack.append(root.right)
        return res[::-1]

        '''
        stack, res =[], [] 

        while stack or root:
            while root:
                stack.append([root,1])
                root = root.left
            root, seen = stack[-1]
            if seen==2:
                root,seen = stack.pop()
                res.append(root.val)
                root=None
            else:
                stack[-1][1] = 2
                root = root.right
        return res


                
