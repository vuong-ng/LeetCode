# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # redo 1
        # iteration
        if not q and not p:
            return True
        if not q or not p:
            return False
        queue = [(q,p),]
        while queue:
            node1, node2 = queue.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            else:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True

        


        # recursion
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)


        #recursion
        
        # if not p and not q:
        #     return True
        # elif not p or not q:
        #     return False
        # elif p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False
        
        #iteration
        stack = [(p,q),]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        return True
            

            