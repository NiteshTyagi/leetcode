class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in ops:
            if i=='D':
                stack.append(2*stack[-1])
            elif i=='C':
                stack.pop()
            elif i=='+':
                stack.append(stack[-2]+stack[-1])
            else:
                stack.append(int(i))
        return sum(stack)
