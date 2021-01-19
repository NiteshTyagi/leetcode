class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[S[0]]
        top=0
        for i in range(1,len(S)):
            if stack:
                if S[i]!=stack[top]:
                    stack.append(S[i])
                    top+=1
                else:
                    stack.pop()
                    top-=1
            else:
                stack.append(S[i])
                top+=1
        return "".join(stack)
        
