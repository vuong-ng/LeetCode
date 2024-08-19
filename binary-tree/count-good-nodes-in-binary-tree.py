# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #re-do 1:
        res = 0
        def dfs(node,prev):
            if not node:
                return 0
            elif node.val >= prev.val:
                return 1 + dfs(node.left, node) + dfs(node.right, node)
            else:
                return dfs(node.left, prev) + dfs(node.right, prev)
        return dfs(root,root)

        #DFS recursion
        """
        self.count = 0

        def dfs(root, max_prev):
            if not root: return 
            if root.val >= max_prev:
                self.count += 1
                max_prev = root.val
            dfs(root.left, max_prev)
            dfs(root.right, max_prev)
        
        dfs(root, float("-inf"))
        return self.count
        """

        #DFS iteration
        # stack = [[root, float('-inf')]]
        # count = 0
        # while stack:
        #     node, max_prev = stack.pop()
        #     if node.val >= max_prev:
        #         count += 1
        #         max_prev = node.val
        #     if node.left: stack.append([node.left, max_prev])
        #     if node.right: stack.append([node.right, max_prev])
        # return count





                      

