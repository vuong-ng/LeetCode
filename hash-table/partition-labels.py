class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}
        freq = 0
        l = 0
        substr = set()
        res = []
        for i in s:
            counter[i] = counter.get(i,0) + 1
        for w in s:
            l += 1
            if w in substr:
                freq -= 1
            else:
                substr.add(w)
                freq = freq + counter[w] - 1
            if freq == 0:
                res.append(l)
                l = 0
        return res


            



        