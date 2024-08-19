class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total//2

        if len(nums1) > len(nums2): #make sure nums1 always smaller than nums2
            nums1, nums2 = nums2, nums1

        #since there is guaranteed to be a median, put a while True loop there
        l,  r = 0, len(nums1) -1
        while True:
            i = (l+r) //2
            j = half - i - 2

            nums1Left = nums1[i] if i >= 0 else float('-inf')
            nums1Right = nums1[i+1] if i < len(nums1) - 1 else float('inf')
            nums2Left = nums2[j] if j >= 0 else float('-inf')
            nums2Right = nums2[j+1] if j < len(nums2) - 1 else float('inf')

            #comparison
            if nums1Left <= nums2Right and nums1Right >= nums2Left:
                #odd nums of elements 
                if total%2 != 0:
                    return min(nums2Right, nums1Right)
                else:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) /2 
            if nums1Left > nums2Right:
                r -= 1
            else:
                l += 1
            
