class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2_map = {}
        mapping = [0] * len(nums1)
        for i in range(len(nums2)):
            nums2_map[nums2[i]] = i
        for j in range(len(nums1)):
            mapping[j] = nums2_map[nums1[j]]
        return mapping