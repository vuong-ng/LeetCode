class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = s[0]
        res = ''
        for i in range(len(s)):
            l, r = i-1, i+1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                temp = s[l:r+1]
                l, r = l-1, r+1
            if len(res) < len(temp):
                res = temp
        
        for i in range(len(s)):
            l, r = i, i+1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                temp = s[l:r+1]
                l,r = l-1, r+1
            if len(res) < len(temp):
                res = temp
        return res

















        # redo 1
        # res = ''
        # for i in range(len(s)):
        #     l, r = i, i 
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if r-l+1 > len(res):
        #             res = s[l:r+1]
        #         l -=1
        #         r += 1
            
            
        #     l, r = i, i+1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if r-l+1 > len(res):
        #             res= s[l:r+1]
        #         l -= 1
        #         r += 1
        # return res


        # res = []
        # substr = ''
        # def dfs(i, substr):
        #     if i > len(s) - 1:
        #         res.append(substr)
        #         substr = ''
        #         return 
        #     substr = substr + s[i]
        #     dfs(i+1, substr)
        #     substr = substr[0:len(substr)-1]
        #     dfs(i+1, substr)
        
        # def isPalindrome(s):
        #     if len(s) <= 1:
        #         return True
        #     if s[0] != s[-1]:
        #         return False
        #     return isPalindrome(s[1:-1])
        # longest = ''
        # for s in res:
        #     if isPalindrome(s) and len(s) > len(longest):
        #         longest = s
        # return longest
            
                
        