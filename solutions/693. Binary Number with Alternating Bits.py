class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def returnNext(r):
            return 0 if r==1 else 1
            
        r = n%2
        n = n//2
        nextBit = returnNext(r)
        while n:
            r = n%2
            n = n//2
            if nextBit==r:
                nextBit = returnNext(r)
            else:
                return False
        return True
