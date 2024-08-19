# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # redo 1
        # bottom-up ver
        def dfs(node):
            if not node:
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)[0]

        
        # top-down version
        if not root:
            return True
        def height(node):
            if not node:
                return 0
            return max(height(node.left)+1, height(node.right)+1)
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        #top-down approach
        """
        if not root:
             return True

        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        if abs(height(root.left) - height(root.right)) > 1: #the tallest tree is not balanced just return False
                                                             ## else: we have to check all of its subtree
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        """
        #bottom-up approach
        
        # def dfs(root):
        #     if not root:
        #         return [True, 0]
        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
        #     return [balanced, 1 + max(left[1], right[1])]  
        # return dfs(root)[0]
        
        
        
        