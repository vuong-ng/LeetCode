class Solution:
    def letterCombinations(self, digits: str) -> List[str]: 
        res = []
        num_char = {"1": [], "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(curStr, j):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for e in range(len(num_char[digits[j]])):
                curStr = curStr + num_char[digits[j]][e]
                backtrack(curStr, j+1)
                curStr = curStr[:-1]
        
        if len(digits) == 0:
            return res
        backtrack("", 0)
        return res


        