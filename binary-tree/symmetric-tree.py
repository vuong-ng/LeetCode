# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            if tree1.val == tree2.val:
                return dfs(tree1.left, tree2.right) and dfs(tree1.right, tree2.left)
            # else: return False
        if not root:
            return True
        return dfs(root.left, root.right)
                
        # return dfs(root)
        # if not root:
        #     return True
        # if root.left and root.right:
        #     if root.left.val == root.right.val:
        #         return dfs(root)
        # return False