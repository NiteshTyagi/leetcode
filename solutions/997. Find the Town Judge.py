class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = [0]*(N+1)
        for a,b in trust:
            d[a]-=1
            d[b]+=1
            
        for i in range(1,N+1):
            if d[i]==N-1:
                return i
        return -1
