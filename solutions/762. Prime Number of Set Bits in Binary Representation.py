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
        # print(setBit)
        
        countP=0
        def checkPrime(n):
            cp=0
            for i in range(1,n+1):
                if n%i==0:
                    cp+=1
                    
            return True if cp==2 else False
                
        for i in setBit:
            if checkPrime(i):
                countP+=1
        return (countP)
