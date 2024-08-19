class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps= 0
        i = 0
        while i < len(logs):
            if logs[i] == "../":
                steps -= 1 if steps > 0 else 0
            if re.findall("\w", logs[i]):
                steps +=1
            i+=1
        return steps
        
        