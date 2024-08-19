class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        for node in edges[0]:
            for i in range(0, len(edges)):
                if node not in edges[i]:
                    break
                elif i == len(edges) -1:
                    return node


        # if len(edges) == 0:
        #     return 0
        # for n in edges[0]:
        #     for e in range(1, len(edges)):
        #         if n not in edges[e]:
        #             break
        #         elif e == (len(edges)-1):
        #             return n
        
        # freq = []
        # if len(edges)==1:
        #     return edges[0][0]
        # for i in range(len(edges[0])):
        #     if edges[1][i] in edges[0]:
        #         return edges[1][i]


    

        