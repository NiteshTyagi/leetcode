class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack =[]
        for i in S:
            if i=='(':
                stack.append(i)
            else:
                top = stack.pop()
                if top=='(':
                    stack.append(1)
                else:
                    result=0
                    while top!="(":
                        result+=top
                        if not stack:
                            break
                        top = stack.pop()
                    stack.append(2*result)
        return sum(stack)
       
# #        Another Solution
#        stack = [0] #The score of the current frame

#         for x in S:
#             if x == '(':
#                 stack.append(0)
#             else:
#                 v = stack.pop()
#                 stack[-1] += max(2 * v, 1)

#         return stack.pop()
        
