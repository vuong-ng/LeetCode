# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if len(arr) < 1:
                return None
            curr = TreeNode(arr[len(arr)//2])
            curr.left = dfs(arr[:len(arr)//2])
            curr.right = dfs(arr[len(arr)//2 + 1:])
            return curr
        return dfs(nums)
 

        if len(nums) == 0:
            return None
        m = len(nums)//2 
        head = TreeNode(nums[m])
        left = m-1
        right = m+1


        