class Solution:
    def minOperations(self, logs: List[str]) -> int:
        root=0
        for i in logs:
            if i=='../':
                if root!=0:
                    root-=1
            elif i=='./':
                pass
            else:
                root+=1
        return root
                
        
