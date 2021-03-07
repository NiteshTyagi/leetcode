class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nth_bits = 1<<n
        for i in range(2**n):
            bitmask = bin(i|nth_bits)[3:]
            
            result.append([nums[j] for j in range(n) if bitmask[j]=='1'])
​
        return result
