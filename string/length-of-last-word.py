class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = s.split(" ")
        for e in range(len(ls)-1,-1,-1):
            if ls[e] != "":
                return len(ls[e])
        return 0