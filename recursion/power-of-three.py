class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #recursion
        """
        n = float(n)
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n/3)
        """
        if n < 1:
            return False
        while n % 3==0:
            n /= 3
        return n == 1
