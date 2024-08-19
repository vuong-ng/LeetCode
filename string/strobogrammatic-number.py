class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #rotate hash map
        """
        res = ''
        rotate = {'8':'8', '6':'9', '9':'6', '1':'1', '0':'0'}
        for i in range(len(num)):
            if num[i] in rotate:
                res = rotate[num[i]] + res
            else:
                return False
        return num==res
        """
        #2 pointers
        left = 0
        right = len(num)-1
        rotate = {'8':'8', '6':'9', '9':'6', '1':'1', '0':'0'}
        while left<=right:
            if num[left] not in rotate or rotate[num[left]] != num[right]:
                return False
            else:
                left+=1
                right-=1
        return True



        """

        num = int(num)
        if num == 0 or num==8 or num == 1:
            return True
        elif num%10 == 1:
            while num > 0:
                r = num%10 
                if r != 1:
                    return False
                elif num%10 == 1: 
                    num = num//10
            return True

        elif num%10 == 8:
            while num > 0:
                r = num%10 
                if r != 8:
                    return False
                elif num%10 == 8: 
                    num = num//10
            return True

        elif len(str(num)) %2==0 and (num%10 == 6 or num%10==9):
            i = len(str(num))-2
            if num%10 == 6:
                if str(num)[i] != "6" or str(num)[i-1] != "9":
                    return False
                i-=1
                if i <0:
                    return True
            elif num%10 == 9:
                if str(num)[i] != "9" or str(num)[i-1] != "6":
                    return False
                i-=1
                if i <0:
                    return True
        return False
        """
