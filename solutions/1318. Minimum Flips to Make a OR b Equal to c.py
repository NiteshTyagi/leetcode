class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        nth_bit = 1<<32
        a = bin(a|nth_bit)[3:]
        b = bin(b|nth_bit)[3:]
        c = bin(c|nth_bit)[3:]
        for i in range(32):
            if c[i]=='1':
                if a[i]=='0' and b[i]=='0':
                    count+=1
            else:
                if a[i]=='1' and b[i]=='0':
                    count+=1
                elif a[i]=='0' and b[i]=='1':
                    count+=1
                elif a[i]=='1' and b[i]=='1':
                    count+=2
                    
        return (count)
        
