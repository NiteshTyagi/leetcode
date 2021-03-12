class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        return list(filter(lambda x:x[1]==1,count.items()))[0][0]
