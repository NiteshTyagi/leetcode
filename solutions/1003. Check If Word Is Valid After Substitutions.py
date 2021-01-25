class Solution:
    def isValid(self, s: str) -> bool:
        if s[0]!='a':
            return False
        
        stack = [s[0],]
        for i in range(1,len(s)):
            if stack:
                if s[i]=='b' and stack[-1]=='a':
                    stack.pop()
                    stack.append(s[i])
                elif s[i]=='c' and stack[-1]=='b':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return True if not stack else False
        
