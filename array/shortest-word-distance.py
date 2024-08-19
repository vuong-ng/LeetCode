class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = len(wordsDict)
        f1 = -len(wordsDict)
        f2 = len(wordsDict)
        both_found = False
        for i in range (len(wordsDict)):
            if wordsDict[i] == word1:
                f1 = i
            elif wordsDict[i] == word2:
                f2 = i 
            temp = abs(f1-f2)
            if temp < res:
                res = temp
        return res



