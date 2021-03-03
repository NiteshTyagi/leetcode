class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)//2
        from collections import Counter
        count = Counter(nums)
        return list(filter(lambda x:x[1]>size ,count.items()))[0][0]
