class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""

        while columnNumber > 0:
            res = res + chr(((columnNumber-1)%26) + 65) 
            columnNumber = (columnNumber-1)//26
        return res[::-1]