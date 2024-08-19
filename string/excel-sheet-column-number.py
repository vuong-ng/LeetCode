class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        exp = 0
        res = 0
        for i in range(len(columnTitle)-1,-1,-1):
            res+= (ord(columnTitle[i])+1-65) * (26 ** exp)
            exp+=1
        return res