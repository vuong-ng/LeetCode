# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case: when the current node is a leaf node 
        # iterate through the tree from root
        # if the val is less than the current node value -> the move to the left branch
        # else move to the right branch
        def insert(node):
            if not node:
                return TreeNode(val)
            else:
                if val > node.val:
                    node.right = insert(node.right)
                else:
                    node.left = insert(node.left)
                return node
        res = insert(root)
        return res


        