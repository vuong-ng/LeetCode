# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None): 
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        #iterative
        """
        if root == None:
            return root
        stack = [root]
        sub = abs(target - root.val)
        ans = root.val
        while stack:
            node = stack.pop()
            if abs(target - node.val) < sub:
                ans=node.val
                sub =  abs(target - node.val)
            elif abs(target-node.val) == sub:
                if ans > node.val:
                    ans = node.val 
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans
        """
        #recursive:
        """
        num = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            num.append(root.val)
            traverse(root.right)
            num.append(root.val)
            return num
        num= traverse(root)
        return min(num, key = lambda x: abs(target-x))
        """
        #shorter recursive
        """ 
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return min(inorder(root), key = lambda x: abs(target-x))
        """

        #Iterative: stop right when the closest value is found
        """
        stack, pred = [], float('-inf')

        while stack or root:
            while root:  #go as left as you can
                stack.append(root)
                root = root.left
            root=stack.pop()
            if target >= pred and target < root.val:
                if abs(target - pred) == abs(target - root.val):
                    return min(root.val, pred)
                return min(root.val, pred, key = lambda x: abs(target-x))
            pred = root.val
            root = root.right
        return pred #if the closest value is not found in the loop => the last one must he be last one
        """

        #Binary search 
        closest = root.val
        while root:
            #if abs(target -closest) == abs(target -root.val):
                #cloesest = min(closest, root.val)
            closest = min(closest, root.val, key = lambda x: (abs(target - x), x))
            if target > root.val:
                root = root.right
            else: root=root.left
        return closest
