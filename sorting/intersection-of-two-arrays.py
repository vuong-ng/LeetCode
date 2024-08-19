class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #brute force
        """
        res= []
        for i in range(len(nums2)):
            if nums2[i] in res:
                continue
            elif nums2[i] in nums1:
                res.append(nums2[i])
        return res
        """
        #built-in set intersection
        set1 = set(nums1)
        set2 = set(nums2)
        return (set1 & set2)



