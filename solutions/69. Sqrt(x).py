class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        while l<=r:
            mid=(l+r)//2
            if mid*mid<=x< (mid+1)*(mid+1):
                return mid
            elif mid*mid<x:
                l=mid+1
            else:
                r=mid-1
        return 0
