class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #draft
        """
        stack = []
        #if len(heights) <=1:
        #    return heights[0]

        for i in range(len(heights)-1):
            area = min(heights[i], heights[i+1]) * 2
            if area < heights[i]:
                area = heights[i]
            if not stack or area > stack[-1][0]:
                stack.append((area, heights[i], i))
        
        def combine_heights(height_stack):
            while len(stack) > 1:
                height = stack.pop()
                a, h, i = height[0], height[1], height[2]
                height1 = stack.pop()
                a1, h1, i1 = height1[0], height[1], height[2]
                area = min(a, a1) * (i-i1+1)
                if (min(a, a1) * (i-i1+1)) > a and (min(a, a1) * (i-i1+1)) > a1:
                    stack.append(area)
                else:
                    stack.append((a,h,i))
            return stack[-1][0]

        return combine_heights(stack)
        """
        maxArea = 0
        stack = [] #pair: index and height
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea





            
            
