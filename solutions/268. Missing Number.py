class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        actualSum  = sum(range(size+1))
        expectedSum = sum(nums)
        return actualSum - expectedSum
