class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        if len(s)!=len(t):
            return False
        for i in 'abcdefghijklmnopqrstuvwxyz':
            d[i]=0
            
        for i in range(len(s)):
            d[s[i]]+=1
            d[t[i]]-=1
            
        return all(i==0 for i in d.values())
