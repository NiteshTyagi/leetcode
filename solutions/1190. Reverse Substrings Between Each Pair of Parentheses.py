class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i==')':
                temp_str,popped='',''
                while (popped!='('):
                    temp_str+= popped
                    popped = stack.pop()[::-1]
                stack.append(temp_str)
            else:
                stack.append(i)
        return "".join(stack)
        
