class Solution:
    def interpret(self, command: str) -> str:
        return "o".join(command.split('()')).replace('(','').replace(')','')
        # stack = []
        # for i in command:
        #     if i==')':
        #         element = stack.pop()
        #         s_temp=''
        #         while element!='(':
        #             s_temp+=element
        #             if not stack:
        #                 break
        #             element=stack.pop()
        #         if s_temp:
        #             stack.append(s_temp[::-1])
        #         else:
        #             stack.append('o')
        #     else:
        #         stack.append(i)
        # return "".join(stack)
        
