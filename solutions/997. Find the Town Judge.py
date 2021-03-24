class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = {i:[0,0] for i in range(1,N+1)}
        # print(d)
        for a,b in trust:
            d[b][0]+=1
            d[a][1]+=1
        # print(d)
        f=list(filter(lambda x:True if x[1][0]==N-1 and x[1][1]==0 else False,d.items()))
        return f[0][0] if len(f)==1 else -1
        
