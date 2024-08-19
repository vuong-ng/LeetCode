class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        if len(needle)>len(haystack):
            return -1
        for n in range(len(haystack)):
            j=n
            for m in range(len(needle)):
                if needle[m] != haystack[j]:
                    break
                elif m==len(needle)-1:
                    return n
                j+=1

        return -1
        '''
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        if n<m:
            return -1
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1
