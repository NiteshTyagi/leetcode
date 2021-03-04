class Solution:
    def reverseBits(self, n: int) -> int:
        r,power = 0,31
        while n:
            r+=(n&1)<<power
            # print(r,end='')
            n>>=1
            power-=1
        return r
