class Solution:
    def check_constraint(self,result):
        return -2**31<=result<=2**31-1
    
    def reverse(self, x: int) -> int:
        if self.check_constraint(x):
            if x>0:
                x=str(x)    
                result = int(x[::-1])
            elif x<0:
                x=str(x)
                result = -int(x[:0:-1])
            else:
                return 0
            return result if self.check_constraint(result) else 0
        else:
            return 0
