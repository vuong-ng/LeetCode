class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i =0
        while i < len(s):
            if s[i] ==']':
                temp = ''
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                n=''
                while stack and stack[-1].isnumeric():
                    n = stack.pop() + n
                n=int(n)
                while n:
                    stack.append(temp)
                    n-=1
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)
                    
