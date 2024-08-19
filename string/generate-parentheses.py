class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr_str, open_count, close_count):
            if open_count == close_count == n:
                res.append(curr_str)
                return
            if open_count < n:
                # curr_str += "("
                backtrack(curr_str+ "(", open_count+1, close_count)
            if open_count > close_count:
                # curr_str += ")"
                backtrack(curr_str + ")", open_count, close_count+1)
        backtrack("",0,0)
        return res


















        stack = []
        res = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if openN > closeN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0,0)
        return res
            
                
