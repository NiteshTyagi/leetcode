class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        k = 0 
        stack = []
        while (i<len(pushed) and k<len(popped) ):
            if stack and stack[-1]==popped[k]:
                stack.pop()
                k+=1
            else:
                stack.append(pushed[i])
                i+=1
        print(stack,k,i)
        for i in popped[k:]:
            if i == stack[-1]:
                stack.pop()
        return True if not stack else False
        
