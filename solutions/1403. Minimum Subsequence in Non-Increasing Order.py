class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        result = [nums[0]]
        i=1
        while i<len(nums):
            if sum(result)>sum(nums[i:]):
                return result
            else:
                result.append(nums[i])
            i+=1
        return result
                
        
