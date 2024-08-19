# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # redo 2:
        # iterate down the tree and count the k to 0
        # first move to the left
        # then move to the right
        # if the k reach 0: return the current node's value
        # n = [k,]
        # iterative
        # usual inorder traversal
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            if k == 0:
                return root.val
            root=root.right

            
        

        # recursion
        nums = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)
        return nums[k-1]













        # redo 1
        # inorder recursion
        # res = 0
        # nums = []
        # def dfs(root):
        #     if not root:
        #         return 
        #     dfs(root.left)
        #     nums.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return nums[k-1]

        #iterative
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0 :
                return root.val
            root = root.right
        
        
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            if not k: return node.val
            else: k -= 1
            if node.left:
                while node:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        """
        #inorder recursion
        """
        nums = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root)
        return nums[k-1]
        """
        #inorder iteration
        # stack = []
        # cur = root
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     k -= 1
        #     if k== 0: 
        #         return cur.val
        #     cur = cur.right
            

        
        
            