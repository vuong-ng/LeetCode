class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        #checked = set()
        left = 0
        right = len(height) -1
        while height[left] == 0 or height[right] == 0:
            if height[left] == 0:
                left+=1
            if height[right] == 0:
                right-=1

        highest_wall = min(height[left], height[right])
        vol = highest_wall * (len(height[left+1:right]))
        while left < right:
            if height[right] == 0:
                right -=1
                
            elif height[left] == 0:
                left +=1
                
    
            elif height[left] != 0 and height[right] !=0:
                curr_wall = min(height[right], height[left])
                #vol = vol - min(height[right], highest_wall) - min(height[left], highest_wall)
            #update volume:
                if curr_wall > highest_wall:
                    vol += (len(height[left+1:right])) * (curr_wall - highest_wall)
            #subtract the volume from the position in which the wall is placed.
                vol = vol - min(height[left], highest_wall) - min(height[right], highest_wall)
                highest_wall = max(highest_wall, curr_wall)
                left +=1
                right-=1

        if left == right:
            vol -= min(height[left], highest_wall)
        return vol
        """
        l, r = 0, len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        res = 0
        while l < r:
            if maxLeft < maxRight:
                l +=1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -=1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res


            



