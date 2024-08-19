# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        #stack = []
        root = 0
        res = TreeNode(preorder[root])

        cur = res
        stack = [cur,]
        while stack and cur:
            cur = stack.pop()
            i = inorder.index(cur.val)
            left = inorder[i - 1] if i > 0 else None
            right = inorder[i+1] if i < len(inorder) - 1 else None
            cur.left = TreeNode(left)
            cur.right = TreeNode(right)
            if right:
                stack.append(cur.right)
            if left:
                stack.append(cur.left)
            #root += 1
        return res
        """
        """
        if not preorder: return

        mid = inorder.index(preorder[0])
        root = TreeNode(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        """
        """
        inorderHash = {}
        for i, val in enumerate(inorder):
            inorderHash[val] = i
        
        def build(preorder, inorder):
            if not preorder or not inorder: return

            mid = inorderHash[preorder[0]]
            root = TreeNode(preorder[0])

            root.left = build(preorder[1: mid+1], inorder[:mid])
            root.right = build(preorder[mid+1:], inorder[mid+1:])
            return root
        return build(preorder, inorder)
        """
        inorderHash = {}
        for i, val in enumerate(inorder):
            inorderHash[val] = i
        
        self.cur = 0
        def build(left, right):
            if left > right or right < left:
                return None
            
            mid = inorderHash[preorder[self.cur]]
            root = TreeNode(preorder[self.cur])

            self.cur +=1
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        return build(0, len(preorder) - 1)









            
            

