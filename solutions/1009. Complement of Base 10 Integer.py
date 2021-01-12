class Solution:
    def bitwiseComplement(self, N: int) -> int:
        comp_binary = [int(c)^1 for c in bin(N)[2:]][::-1]
        print(comp_binary)
        r=0
        for i in range(len(comp_binary)):
            r+=(2**i)*(comp_binary[i])
        return r
