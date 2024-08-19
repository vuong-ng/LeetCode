class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # iterate from the back of the array
        stack = []
        res =[0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                val, index = stack.pop()
                res[index] = i - index
            stack.append((temp,i))
        
        return res























        res = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and s[-1][0] < t:
                temp, d = s.pop()
                res[d] = i-d
            s.append([t,i])
        return res


            




















        # res = [0] * len(temperatures)
        # stack = []
        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]: #check stack before calling stack[-1]
        #         temp, d = stack.pop()
        #         res[d] = i-d
        #     stack.append((t, i))
        # return res

