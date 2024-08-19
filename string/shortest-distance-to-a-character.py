class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [len(s)+1] * len(s)
        finds = []
        for i,char in enumerate(s):
            if char == c:
                finds.append(i)
                res[i] = 0
        for index in finds:
            q = [index,]
            visit = set()
            while q:
                curr_index = q.pop(0)
                visit.add(curr_index)
                directions = [1,-1]
                for dr in directions:
                    if curr_index+dr in range(len(s)) and res[curr_index+dr] > res[curr_index]+1 and curr_index+dr not in visit:
                        res[curr_index+dr] = res[curr_index] + 1
                        visit.add(curr_index)
                        q.append(curr_index+dr)
        return res
            
            

        