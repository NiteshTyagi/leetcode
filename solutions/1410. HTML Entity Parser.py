class Solution:
    def entityParser(self, text: str) -> str:
        entity = {
            '&quot;'        : '\"',
            '&apos;'        : "\'",
            '&amp;'         : '&',
            '&gt;'          : '>',
            '&lt;'          : '<',
            '&frasl;'       : '/',
        }
        stack = []
        for st in text:
            stack.append(st)
            if st==';':
                s_temp=''
                element = stack.pop()
                while element!='&' and stack:
                    s_temp+=element[::-1]
                    element = stack.pop()
                s_temp+=element[::-1]
                s_temp = s_temp[::-1]
                if s_temp in entity:
                    stack.append(entity[s_temp])
                    stack.append('\\')
                else:
                    stack.append(s_temp)
                
        return "".join(stack).replace("\\","")
