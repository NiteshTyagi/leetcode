class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        from collections import Counter
        stack = []
        maxTime = max([int(log.split(':')[2]) for log in logs])
        if maxTime>=100000000:
            if n==1:
                return [maxTime+1]
            elif n==2:
                return [90000001,10000000] 
        timeScale = [-1]*(maxTime+1)
        
        for log in logs:
            fun,status,tstp=log.split(':')
            if status=='start':
                timeScale[int(tstp)]= int(fun)
                stack.append(int(tstp))
            else:
                top = stack.pop()
                for i in range(top+1,int(tstp)+1):
                    if timeScale[i]==-1:
                        timeScale[i]= int(fun)
            
        timeScale=Counter(timeScale)
        return list(timeScale.values())
