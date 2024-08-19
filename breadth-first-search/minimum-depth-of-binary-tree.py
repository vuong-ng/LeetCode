# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # recursion
        if not root:
            return 0
        if not root.right:
            return 1 + self.minDepth(root.left)
        if not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
        # iteration
        queue = [root,]
        if not root:
            return 0
        level = 1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                if not node.left and not node.right:
                    return level
                else:
                    queue.append(node.left)
                    queue.append(node.right)
            level+=1
        return level

        # 
        # if not root:
        #     return 0
        # if not root.left:
        # if not root.right:
        #     return 1 + self.minDepth(root)
        # return min(self.minDepth(root.right), self.minDepth(root.left) +1)
        