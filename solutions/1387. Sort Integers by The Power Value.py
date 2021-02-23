class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        result = []
        for i in range(lo,hi+1):
            p = i
            count=0
            while p!=1:
                if p%2==0:
                    p = p//2
                else:
                    p = 3*p+1
                count+=1
            result.append((i,count))
        result.sort(key=lambda x:x[1])
        return result[k-1][0]
        
