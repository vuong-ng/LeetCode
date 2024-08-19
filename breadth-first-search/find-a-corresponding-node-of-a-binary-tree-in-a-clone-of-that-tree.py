# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        #recursive
        """
        if not original:
            return None
        elif original == target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
        """
        def inorder(root):
            if not root:
                return None
            else:
                if root.val == target.val:
                    return root
            return inorder(root.left) or inorder(root.right)
        return inorder(cloned)
        
        #iterative
        """
        stack =[cloned]
        while stack or cloned:
            if cloned:
                cloned = cloned.left
                stack.append(cloned)
            if not cloned:
                node = stack.pop()
                if node.val == target.val:
                    return node
                stack.append(node.right)
        """
    


        
