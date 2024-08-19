class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4!=0
        """
        def count_step(i, n):
            if i < n:
                count+=1
                count_step(i+1,n) 
                count_step(i+2,n)
                count_step(i+3,n)
            elif i == n:
                if count
        """