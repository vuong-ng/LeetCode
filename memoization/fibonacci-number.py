class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #recursive O(2^n)
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return self.fib(n-2) + self.fib(n-1)
        """
        #top-down approach using memoization
        """
        cache = {0:0, 1:1}
        def comp_fib(cache, n):
            if n in cache:
                return cache[n]
            cache[n] = comp_fib(cache, n-1) + comp_fib(cache, n-2)
            return cache[n]
        return comp_fib(cache, n)
        """
        #bottom-up
        """
        if n <= 1:
            return n
        cache = [0] * (n+1) # create a list of n+1 0s
        cache[1] = 1
        for i in range(2, n+1):
            cache[i] = cache[i-1] +cache[i-2]
        return cache[n]
        """
        # iterative bottom-up 
        if n<=1:
            return n
        prev1 = 0
        prev2 = 1
        current = 0
        for i in range(n):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current


        

        