# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        # add the max height of left branch with the max heihgt of right branch

        def dfs(root):
            if not root: 
                return 0
            left = dfs(root.left)
            right =dfs(root.right)
            res[0] = max(res[0], left + right)
            return max(left, right) +1
        dfs(root)
        return res[0]
            
            













        res = [0]

        def longestPath( root):
            if not root:
                return -1
            #nonlocal diameter
            left = longestPath(root.left)
            right = longestPath(root.right)
            res[0] = max(res[0], 2 + left + right)
            return max(left, right) + 1
        longestPath(root)
        return res[0]