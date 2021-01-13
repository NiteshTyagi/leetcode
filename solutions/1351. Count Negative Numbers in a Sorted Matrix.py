class Solution:
    def bineary_search(self,A,l,r):
        if l<=r:
            mid=(l+r)//2
            if A[mid]>=0:
                if A[l]>=0:
                    return l
                else:
                    return self.bineary_search(A,l,mid)
            else:
                return self.bineary_search(A,mid+1,r)
        else:
            return 0
        
    def countNegatives(self, grid: List[List[int]]) -> int:
        sorted_listed=[]
        for i in grid:
            sorted_listed.extend(i)
        if len(sorted_listed)>1:
            sorted_listed.sort()
            return self.bineary_search(sorted_listed,0,len(sorted_listed)-1)
        else:
            return 1 if sorted_listed[0]<0 else 0
        
        
