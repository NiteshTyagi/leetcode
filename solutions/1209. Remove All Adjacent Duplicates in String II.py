class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=''
        for i in s:
            stack+=i
            if len(stack)>=k:
                if stack[-k:]==i*k:
                    stack = stack[:-k]
        return stack
        
