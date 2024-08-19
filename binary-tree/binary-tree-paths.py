# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # iterative ver.
        stack = [(root, str(root.val)),]
        paths = []
        while stack:
            node, path = stack.pop()
            if node.left:
                stack.append((node.left, path+"->"+str(node.left.val)))
            if node.right:
                stack.append((node.right, path+"->"+str(node.right.val)))
            elif not node.left and not node.right:
                paths.append(path)
        return paths

        # recursive ver.
        # paths = []
        # def dfs(node,path):
        #     if node:
        #         path += str(node.val)
        #         if not node.left and not node.right:
        #             paths.append(path)
        #         path += "->"
        #         dfs(node.left, path)
        #         dfs(node.right, path)
        # dfs(root, "")
        # return paths

            
            

        