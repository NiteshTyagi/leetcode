class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        result=0
        while num:
            result+=1
            if num&1:
                num-=1
            else:
                num = num>>1
                          
        return result
        
