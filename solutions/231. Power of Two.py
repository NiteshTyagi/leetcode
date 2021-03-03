class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0:
            from math import log
            x = int(log(n)/log(2))
            return True if 2**x==n else False
        else:
            return False
