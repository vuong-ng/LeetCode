class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        def flip(s, A, B):
            res = ''
            for i in range(len(s)):
                if i == A or i == B:
                    res += '-'
                else: res+=s[i]
            return res
        B = 1
        res = []
        for i in range(len(currentState)-1):
            if currentState[i] == '+' and currentState[B] == '+':
                res.append(flip(currentState, i, B))
            B+=1
            continue
        return res
