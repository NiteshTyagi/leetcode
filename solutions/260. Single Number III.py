class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = list(filter(lambda x: nums.count(x)==1,nums))
        return count
        
