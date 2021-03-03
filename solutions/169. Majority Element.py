class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import Counter
        count = Counter(nums)
        return max(count.keys(),key=count.get)
