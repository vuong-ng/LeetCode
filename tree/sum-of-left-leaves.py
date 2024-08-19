# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #recursive
        """
        def visit(root, isLeft):
            if not root.left and not root.right and isLeft:
                return root.val
            else:
                total = 0
                if root.left:
                    total += visit(root.left, True)
                if root.right:
                    total += visit(root.right, False)
            return total
        return visit(root, False)
        """
        stack = [root,]
        total = 0
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right: 
                total += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return total



