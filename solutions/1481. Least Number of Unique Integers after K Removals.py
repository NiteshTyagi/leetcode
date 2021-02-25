from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        arr = sorted(count.items(),key=lambda x:x[1])
        arr = [list(i) for i in arr]
        i=0
        while k>0:
            if arr[i][1]<=k:
                k = k-arr[i][1]
                arr[i][1]=0
            else:
                arr[i][1]=k
                k=0
            i+=1
        arr = list(filter(lambda x:x[1],arr))
        return len(arr)
