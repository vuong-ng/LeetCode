# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # use stack
        if depth == 1: 
            new_root = TreeNode(val)
            new_root.left = root
            root=new_root
        q = [root,]
        d = 1
        while q:
            d+=1
            for i in range(len(q)):
                node = q.pop(0) 
                if d == depth:
                    # print(node.val, "depth", d)
                    newLeftChild= TreeNode(val)
                    newRightChild = TreeNode(val)
                    if node.left:
                        left_temp = node.left
                        newLeftChild.left = left_temp
                    if node.right:
                        right_temp =node.right
                        newRightChild.right = right_temp
                    node.left = newLeftChild
                    node.right = newRightChild
                    q.append(node.left)
                    q.append(node.right)
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return root
        