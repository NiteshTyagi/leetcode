# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
​
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if isBadVersion(mid)==True:
                if isBadVersion(l)==True:
                    return l
                r=mid-1
            else:
                l=mid+1
        return l
        
