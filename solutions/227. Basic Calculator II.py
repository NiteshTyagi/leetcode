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
                temp = ''
                while i<len(s) and s[i].isdigit():
                    temp+=s[i]
                    i+=1
                operand.append(int(temp))
                i-=1
                
            elif s[i] in ['+','-','/','*']:
                currentop = s[i]
                if s[i]=='/':
                    currentop = '//'
                while (len(operator)!=0 and check_prec(operator[-1]) >= check_prec(currentop)):
                    op1 = operand.pop()
                    op2 = operand.pop()
                    op = operator.pop()
                    result= apply_operator(op2,op1,op)
                    operand.append(result)
                operator.append(currentop)
            i+=1
            
        while len(operator) != 0:
            op1 = operand.pop()
            op2 = operand.pop()
            op = operator.pop()
            result= apply_operator(op2,op1,op)
            operand.append(result)
        return operand[-1]
        
