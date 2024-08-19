# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root,]
        res = []
        while stack:
            temp = []
            for i in range(len(stack)):
                node = stack.pop()
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(temp)
        return res










    # redo 2:
        q = []
        if not root:
            return []
        q = []
        q = [root,]
        res = []
        while q:
            temp=[]
            for i in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     #Recursive
    #     levels = []
    #     if not root:
    #         return levels
    #     def helper(root, level):
    #         if len(levels) == level:
    #             levels.append([])

    #         levels[level].append(root.val)
    #         if root.left:
    #             helper(root.left, level + 1)
    #         if root.right:
    #             helper(root.right, level + 1)
    #     helper(root, 0)
    #     return levels
                
# Re-do 1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q =deque()
        q.append(root)
        res = [[root.val],]
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                # level = []
                if cur.left:
                    level.append(cur.left.val)
                    q.append(cur.left)
                if cur.right:
                    level.append(cur.right.val)
                    q.append(cur.right)
            if len(level) > 0:
                res.append(level)
        return res



        

            