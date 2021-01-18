class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        r=set()
        for i in nums:
            if i in r:
                return i
            r.add(i)
        
