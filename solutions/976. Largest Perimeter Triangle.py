class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A)-3,-1,-1):
            if A[i]+A[i+1]>A[i+2]:
                return sum(A[i:i+3])
        return 0
        
