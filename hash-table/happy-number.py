class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Hashset
        def get_next(n):
          res = 0
          while n > 0:
            res += (n%10)**2
            n = n//10
          return res
        
        hare = get_next(n)
        tortoise = n
        while hare!=1 and hare != tortoise:
          hare = get_next(get_next(hare))
          tortoise = get_next(tortoise)
          if hare == tortoise:
            return False
  
        return hare == 1