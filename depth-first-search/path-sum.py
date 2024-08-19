# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        '''
        def sum(node): 
            s, stack = [], []
            if node:
                s.append(s.val)
            if not node:
                
            if not node.left and not node.right:
                return node.val
            else:
                if node.left:
                    return sum(node.left) + sum(node)
                if node.right:
                    return sum(node.right) +sum(node)
        if not root:
            return False 
        return (sum(root.left)+sum(root)) == targetSum or (sum(root.right)+sum(root)) == targetSum
        '''
        #recursive approach 1
        
        def rootToPath(node, target, curr):
            while node:
                if not node.left and not node.right:
                    curr = curr + node.val
                    if curr == target:
                        return True
                return rootToPath(node.left, target,curr+node.val) or rootToPath(node.right, target,curr+node.val)
        curr = 0
        if not root:
            return False
        else:
            return rootToPath(root, targetSum, curr)
        '''
        #recursie approach 2
        if not root:
            return False
        if not root.left and not root.right:
            targetSum -= root.val
            if targetSum == 0:
                return True
            else:
                return False
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        '''
        #iterative approach
        ###why use stack instead of normal list?
        if not root:
            return False
        stack = [(root, targetSum-root.val)]
        while root or stack:
            node, r = stack.remove(0)
            if not node.left and not node.right:
                if r == 0:
                    return True
            stack.push(root.left, r-root.left.val)
            stack.push(root.right, r - root.right.val)
        return False
            

            
