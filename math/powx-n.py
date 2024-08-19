class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1 
            if n < 0:
                return 1/power(x, -n)
            if n % 2 == 0:
                return power(x*x, n/2)
            if n % 2 != 0:
                return x* power(x * x, (n-1)/2)

        return power(x,n)