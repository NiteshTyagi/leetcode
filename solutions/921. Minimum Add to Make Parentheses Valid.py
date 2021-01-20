class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:return 0
        stack = []
        for i in S:
            if stack:
                if i==')' and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)
                
