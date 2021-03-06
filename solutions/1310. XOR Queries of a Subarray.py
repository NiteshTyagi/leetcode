class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixSum=[arr[0]]
        for i in range(1,len(arr)):
            prefixSum.append(arr[i]^prefixSum[i-1])
        
        result = []
        for L,R in queries:
            if L:
                result.append(prefixSum[R]^prefixSum[L-1])
            else:
                result.append(prefixSum[R])
        
        return result
