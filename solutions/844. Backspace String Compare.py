class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def check(S):
            stack = []
            for i in S:
                if stack and i=='#':
                    stack.pop()
                elif i!='#':
                    stack.append(i)
            return stack
        
        return check(S)==check(T)
