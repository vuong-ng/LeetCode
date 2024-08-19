class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #recursive
        """
        n = float(n)
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfFour(n/4)
        """
        #bit-wise manipulation
        """
        return n > 0 and (n&(n-1)) == 0 and n & 0xaaaaaaaa == 0
        """
        #bit-wise and math
        return n > 0 and (n & (n-1)) == 0 and n%3==1