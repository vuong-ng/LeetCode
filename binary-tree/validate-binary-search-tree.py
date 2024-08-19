# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # redo 2:
        # iterative 
        stack =[]
        prev = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev=root.val
            root=root.right
        return True

        # recursive
        # def dfs(root, left, right):
        #     if not root:
        #         return True
        #     if not(root.val > left and root.val < right):
        #         return False
        #     return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        # return dfs(root, float('-inf'), float('inf'))
           




        #redo 1
        prev= float("-inf")
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev= node.val
            root = node.right
        return True

            














        # stack = []
        # prev = float("-inf")
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
            
        #     node = stack.pop()

        #     if node.val <= prev:
        #         return False
        #     prev = node.val
        #     root = node.right
        # return True

        """
        def valid(root, left, right):
            if not root: return True
            if not(root.val > left and root.val < right):
                return False
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        return valid(root, float("-inf"), float("inf"))
        """

