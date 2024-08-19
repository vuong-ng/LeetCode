class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        h = sorted(height)
        hashmap = {}
        for ind, x in enumerate(height):
            if x not in hashmap:
                hashmap[x] = [ind,]
            else:
                hashmap[x] = [ind] + hashmap[x]
        
        res = min(h[1],h[0])
        j = len(h)-1
        for i in range(len(h)-2, -1, -1):
            left = h[i]
            right = h[j]
            if left == right:
                smallest_ind = hashmap[h[i]][len(hashmap[h[i]]) -1]
                area = abs(hashmap[h[i]][0] - smallest_ind) * h[i]
            else:
                area = abs(hashmap[left][0] - hashmap[right][0]) * min(h[j], h[i])
            if res < area:
                res = area
            j-=1
        return res
        """
        res = min(height[0], height[1])
        left = 0
        right = len(height)-1
        while left < right:
            area = (right-left) * min(height[left], height[right])
            if height[left] <= height[right]:
                left +=1
            elif height[left] > height[right]:
                right -=1
            if area > res:
                res = area
        return res
            



