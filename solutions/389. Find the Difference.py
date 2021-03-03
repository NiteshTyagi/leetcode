class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=0
        for i in s:
            x^=ord(i)
            
        for i in t:
            x^=ord(i)
            
        return chr(x)
