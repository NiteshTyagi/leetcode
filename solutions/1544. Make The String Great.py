class Solution:
    def makeGood(self, s: str) -> str:
        stack =[s[0]]
        for i in range(1,len(s)):
            if stack:
                if s[i]==stack[-1].upper() and s[i].upper()==stack[-1]:
                    stack.append(s[i])
                elif s[i]==stack[-1].upper() or s[i].upper()==stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        print(stack)
        return "".join(stack)
