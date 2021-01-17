class Solution:
    def searchInsert(self, A: List[int], key: int) -> int:
        l=0
        r=len(A)-1
        while l<=r:
            mid= (l+r)//2
            if A[mid]==key:
                return mid
            elif A[mid]<key:
                l=mid+1
            else:
                r=mid-1
        if l>r:
            return r+1
        else:
            return l
        
