class Solution:
    def countBits(self, num: int) -> List[int]:
        if num<0:
            return [0]
        result = [0]*(num+1)
        n=2
        prev = 0
        for i in range(1,num+1):
            if i%n==0:
                n*=2
                result[i]=1
                prev = 1
            else:
                result[i]= result[prev]+1
                prev+=1
        return result
