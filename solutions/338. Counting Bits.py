class Solution:
    def countBits(self, num: int) -> List[int]:
        if num<0:
            return [0]
        result = []
        def countSetBit(i):
            count=0
            while i:
                count+=1
                i = i&(i-1)
            return count
        
        for i in range(0,num+1):
            result.append(countSetBit(i))
        return result
