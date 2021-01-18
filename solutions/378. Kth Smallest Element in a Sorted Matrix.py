class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        r=[]
        for i in matrix:
            r.extend(i)
        r.sort()
        return r[k-1]
        
