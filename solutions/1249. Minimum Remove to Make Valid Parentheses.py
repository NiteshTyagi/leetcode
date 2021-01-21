class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        index =[]
        for i in range(len(s)):
            if stack:
                if s[i]==')' and stack[-1]=='(':
                    stack.pop()
                    index.pop()
                elif s[i] in ['(',')']:
                    stack.append(s[i])
                    index.append(i)
            else:
                if s[i] in ['(',')']:
                    stack.append(s[i])
                    index.append(i)
        stack=[]
        for i in range(len(s)):
            if i not in index:
                stack.append(s[i])
        return "".join(stack)
