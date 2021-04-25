class Solution:
    def calculate(self, s: str) -> int:
        operand = []
        operator = []
        i=0
        
        def check_prec(op):
            if op in ['+','-']:
                return 0
            else:
                return 1 
        def apply_operator(op1,op2,op):
            if op=='+':return op1+op2
            elif op=='-':return op1-op2
            elif op=='*':return op1*op2
            elif op=='//':return op1//op2
        
        while i<len(s):
            if s[i]==' ':
                i+=1
                continue
            elif s[i].isdigit():
                temp = s[i]
                i+=1
                while i<len(s) and s[i].isdigit():
                    temp+=s[i]
                    i+=1
                operand.append(int(temp))
            elif s[i] in ['+','-','/','*']:
                currentop = s[i]
                if s[i]=='/':
                    currentop = '//'
                operator.append(currentop)
            #     if not operator: 
            #         operator.append(currentop)
            #     elif check_prec(currentop) > check_prec(operator[-1]):
            #         operator.append(currentop)
            #     else:
            #         op1 = operand.pop()
            #         op2 = operand.pop()
            #         op = operator.pop()
            #         result= apply_operator(op2,op1,op)
            #         operand.append(result)
            #         operator.append(currentop)
                i+=1
            # print(operand,operator,sep='<-operand--1-1-1-1---operator-->')      
        temp=''
        while operand and operator:
            temp+=str(operand.pop(0))+operator.pop(0)
        temp+=str(operand.pop())
        return eval(temp)
