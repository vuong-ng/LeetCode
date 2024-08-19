class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # while n > 1:
        #     if n % 2 != 0:
        #         return False
        #     n = n // 2
        #     print(n)
        # return n == 1

        temp = 0
        if n < 0:
            return False
        while n:
            temp += n&1
            n >>= 1
        return temp == 1