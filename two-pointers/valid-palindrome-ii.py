class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete = 0
        def recurse(s, isDeleted):
            if len(s) <= 1:
                return True
            if s[0] != s[-1]:
                if isDeleted:
                    return False
                else:
                    isDeleted = True
                    return recurse(s[1:len(s)], isDeleted) or recurse(s[0:-1], isDeleted)
            else: 
                return recurse(s[1:-1], isDeleted)
        return recurse(s, False)