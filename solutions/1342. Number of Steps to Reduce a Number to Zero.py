class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num<1:return 0
        result=-1
        while num:
            # print(num,result)
            result+=1
            if num&1:
                result+=1
                num-=1
            num = num//2
                          
        return result
        
