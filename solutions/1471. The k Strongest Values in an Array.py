class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        index = (len(arr)-1)//2
        median = arr[index]
        result = []
        for i in range(len(arr)):
            result.append((abs(arr[i]-median),arr[i]))
            
        result = list(map(lambda x:x[1],sorted(result,key=lambda x:(x[0],x[1]),reverse=True)))
        
        return result[:k]
