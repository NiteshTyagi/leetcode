class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x^y
        result=0
        while x:
            result+=1
            x = x&(x-1)
        return result
        
