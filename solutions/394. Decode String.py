class Solution:
    def decodeString(self, s: str) -> str:
        if len(s)==1:
            return s
        stack=[]
        flag = False
        s_temp=''
        nums = ['0','1','2','3','4','5','6','7','8','9']
        for i in s:
            if i==']':
                element = stack.pop()
                s_temp=''
                while element!='[':
                    s_temp+=element
                    if not stack:
                        break
                    element = stack.pop()
                element =stack.pop()
                stack.extend(s_temp[::-1]*int(element))
                s_temp=''
            elif i in nums:
                s_temp+=i
                flag=True
            else:
                if flag:
                    stack.append(s_temp)
                    flag=False
                    s_temp=''
                stack.append(i)
        return "".join(stack)
        
