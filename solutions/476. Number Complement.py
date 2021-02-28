class Solution:
    import math
    def findComplement(self, num: int) -> int:
        nob = int(math.floor(math.log(num)/math.log(2))+1)
        return ((1<<nob)-1)^num
        
