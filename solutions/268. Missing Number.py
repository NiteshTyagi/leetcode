class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        for i,v in enumerate(nums):
            
            size^= i^v
            
        return size
