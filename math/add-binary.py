class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s=0
        i=0
        while i <= len(a)-1 or i <= len(b)-1:
            if i > len(a)-1:
                s = s+ int(b[len(b)-1-i])*(2 ** i)
            elif i > len(b)-1:
                s =s + int(a[len(a)-1-i])*(2**i)
            else:
                s += int(a[len(a)-1-i])*(2**i) + (int(b[len(b)-1-i])*(2 ** i))
            i+=1
        res=''
        if s==0:
            return '0'
        while s > 0:
            res= str(s%2) + res
            s=s//2
        return res
