# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # traverse to the target node
        # once reach the target node, start to count back k
        # when k == 0 and node not Null, return the current node's value
        # iterative
        graph = collections.defaultdict(list)
        curr = root
        def build_graph(curr, parent):
            if curr and parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            if curr.left:
                build_graph(curr.left, curr)
            if curr.right:
                build_graph(curr.right, curr)
        build_graph(root, None)
        visited = set([target.val])
        queue = [(target.val, 0)]
        res = []
        while queue:
            nodeval, d = queue.pop(0)
            # visited.add(nodeval)
            if d == k:
                res.append(nodeval)
                continue
            for node in graph[nodeval]:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, d+1))
        return res
            


        # recursive
        def add_parent(curr,parent):
            if not curr:
                return
            if curr:
                curr.parent = parent
                add_parent(curr.left, curr)
                add_parent(curr.right, curr)
        add_parent(root, None)
        visited = set()
        res = []
        def dfs(root, distance):
            if not root or root in visited:
                return
            visited.add(root)
            if distance == 0:
                res.append(root.val)
            dfs(root.left, distance-1)
            dfs(root.right, distance-1)
            dfs(root.parent, distance-1)
        dfs(target, k)
        return res

                

        