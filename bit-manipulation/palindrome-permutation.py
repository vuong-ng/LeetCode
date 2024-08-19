class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else: d[s[i]] +=1
        odd_letter = 0
        for e in d:
            if d[e] % 2==1:
                odd_letter +=1
        return odd_letter ==1 or odd_letter ==0