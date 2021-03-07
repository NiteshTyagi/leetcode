class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor, res1, res2 = 0, 0, 0
        for num in nums:
            xor ^= num
        xor = xor & (~(xor-1))
        for num in nums:
            if num & xor == 0:
                res1 ^= num
            else:
                res2 ^= num
​
        return [res1, res2]
        
        
