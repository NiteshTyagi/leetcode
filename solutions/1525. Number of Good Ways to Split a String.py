class Solution:
    def numSplits(self, s: str) -> int:
        from collections import Counter
        L,R = Counter(),Counter(s)
        good = 0
        
        for i in s[:-1]:
            L[i]+=1
            R[i]-=1
            if R[i]==0:
                del R[i]
                
         
            if len(L)==len(R):
                good+=1
        return good
