# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        next_lv = deque([root,])
        cur_lv = deque()
        res = []
        while next_lv:
            cur_lv = next_lv
            next_lv = deque()
            while cur_lv:
                # cur_lv = next_lv
                node = cur_lv.popleft()
                # next_lv = deque()
                if node.left:
                    next_lv.append(node.left)
                if node.right:
                    next_lv.append(node.right)
                # cur
            res.append(node.val)
        return res

    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     rightSide = []

    #     def dfs(root, level):
    #         if level == len(rightSide):
    #             rightSide.append(root.val)
    #         if root.right:
    #             dfs(root.right, level + 1)
    #         if root.left:
    #             dfs(root.left, level + 1)
    #     dfs(root, 0)
    #     return rightSide

        # """
        # #BFS using queue

        # if not root:
        #      return []
        # q = deque([[root],])
        # res = []
        # while q:
        #     nodes = q.popleft()
        #     res.append(nodes[-1].val)
        #     level = []
        #     for node in nodes:
        #         if node.left:
        #             level.append(node.left)
        #         if node.right:
        #             level.append(node.right)
        #     if len(level) > 0:
        #         q.append(level)
        # return res
        # """

# Re-do 1:  
    # BFS
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     q = deque()
    #     q.append(root)
    #     if not root:
    #         return res
    #     res.append(root.val)
    #     val = root.val
    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node.left: 
    #                 val = node.left.val
    #                 q.append(node.left)
    #             if node.right: 
    #                 val = node.right.val
    #                 q.append(node.right)
    #         res.append(val)
    #     return res[:-1] 

    # DFS
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     res =[]
    #     level = 0
    #     if not root:
    #         return res
    #     def dfs(node):
    #         if not node:
    #             return
    #         if len(res) == level:
    #             res.append(node.val)
    #         if node.right:
    #             dfs(node.right, level+1)
    #         if node.left:
    #             dfs(node.left, level+1)
    #     dfs(root, 0)
    #     return res



