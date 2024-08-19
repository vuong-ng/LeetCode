# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        #recursive
        """
        curr1 = root1
        #if not curr1 and not root2: #both trees have reached the leaf nodes => return the result
        #    return root1

        if curr1 and root2:
            curr1.val = (root1.val + root2.val)

        elif not root1 or not root2:
            if not root1:
                return root2
            elif not root2:
                return root1
        curr1.left = self.mergeTrees(curr1.left, root2.left) #this is why we return root1/root2 if root2/root1 is null
        curr1.right =self.mergeTrees(curr1.right, root2.right)
        return root1 #if both roots are null => return root1
        """

        #iterative
        if not root1:
            return root2
        stack = [[root1, root2],]
        while stack:
            nodes = stack.pop()
            if not nodes[1]:
                continue
            nodes[0].val += nodes[1].val
            if not nodes[0].left:
                nodes[0].left = nodes[1].left
            else: stack.append([nodes[0].left, nodes[1].left])
            if not nodes[0].right:
                nodes[0].right= nodes[1].right
            else: 
                stack.append([nodes[0].right, nodes[1].right])
        return root1
        

        
