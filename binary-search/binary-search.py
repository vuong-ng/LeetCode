class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if target < nums[mid]:
                high = mid -1
            elif target > nums[mid]:
                 low = mid + 1
            elif nums[mid] == target:
                return mid
        return -1

