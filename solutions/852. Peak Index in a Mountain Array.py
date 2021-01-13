class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def binary_search(A,l,r):
            if l<=r:
                mid=l+(r-l)//2
                if A[mid]<A[mid-1] :
                    return binary_search(A,l,mid-1) 
                else:
                    return binary_search(A,mid+1,r) 
            else:
                return l-1
        
        # peak_element = max(arr)
        return binary_search(arr,0,len(arr)-1)
        
