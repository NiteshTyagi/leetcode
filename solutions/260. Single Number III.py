class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        return list(map(lambda x:x[0],filter(lambda x: x[1]==1,count.items())))
        
        
