class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count,l_count,result=0,0,0
        for i in s:
            if i=='L':
                l_count+=1
            elif i=='R':
                r_count+=1
            
            if l_count==r_count:
                result+=1
                l_count,r_count=0,0
        return result
        
