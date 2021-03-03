class Solution:
    def hasAlternatingBits(self, n: int) -> bool:    
        r = n&1
        n = n>>1
        while n:
            if n&1==r:
                return False
            r = n&1
            n = n>>1
        return True
