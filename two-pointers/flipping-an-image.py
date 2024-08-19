class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        out = []
        for row in image:
            tmp = [0] * len(row)
            for i in range(len(row)):
                tmp[i] = (1 - row[(len(row) - 1 - i)])
            out.append(tmp)
        return out
        