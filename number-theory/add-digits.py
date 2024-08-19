class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #loop
        """
        def add(num):
            res = 0
            while num >= 10:
                res += num%10
                num = num//10
            return res + num

        while num >= 10:
            num = add(num)
        return num
        """
        #recursion
        """
        if num <10:
            return num
        num = self.addDigits(num//10) + (num%10)
        return self.addDigits(num)
        """
        ##O(1) Digital roots
        return 1+(num-1) % 9 if num else 0
        
