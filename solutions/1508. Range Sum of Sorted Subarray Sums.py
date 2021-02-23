class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = [nums[0]]
        for i in range(1, n):
            ans.append(nums[i])    
            nums[i] += nums[i-1]
            ans.append(nums[i])    
            for j in range(i-1): ans.append(nums[i] - nums[j])
        ans.sort()                
        return sum(ans[left-1:right])%(10**9+7)
        
