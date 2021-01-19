class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        r=[]
        start=1
        for i in range(len(S)):
            if S[i]=='(':
                stack.append(S[i])
            elif S[i]==')':
                stack.pop()
            if len(stack)==0:
                r.append(S[start:i])
                start=i+2
        if r:
            return ''.join(r)
        else:
            ""
        
