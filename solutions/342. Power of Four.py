class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0:
            from math import log
            x = int(log(n)/log(4))
            return True if 4**x==n else False
        else:
            return False
