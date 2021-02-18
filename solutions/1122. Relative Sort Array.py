class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict()
        result = []
        for i in arr1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
​
        for i in arr2:
            if i in d:
                result.extend([i]*d[i])
                d.pop(i)
        for k in sorted(d):
            result.extend([k]*d[k])
​
        return result
