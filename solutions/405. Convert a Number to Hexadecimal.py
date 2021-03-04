class Solution:
    def toHex(self, num: int) -> str:
        result = ''
        if num<0:
            num = 2**32+num
        if num>0:
            while num:
                r = num%16
                if 10<=r<=15:
                    result+=chr(97+r-10)
                else:
                    result+=str(r)
                num//=16
        elif num==0:
            result = '0'
        return(result[::-1])
