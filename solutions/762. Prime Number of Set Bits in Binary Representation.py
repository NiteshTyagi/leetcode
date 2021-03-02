class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        setBit = []
        def countBit(n):
            count = 0
            while n:
                count+=1
                n = n&(n-1)
            if count>1:return count
        
        for i in range(L,R+1):
            countB = countBit(i)
            if countB:
                setBit.append(countB)
        
        countP=0
        PrimeNumbers = [2,3,5,7,11,13,17,19]
                
        for i in setBit:
            if i in PrimeNumbers:
                countP+=1
        return (countP)
