class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        stack = [(0,nums[0]),]
        index = [0]*len(nums)
        
        for i in range(1,len(nums)):
            element = stack.pop()
            while element[1]<nums[i]:
                index[element[0]] = nums[i]
                if not stack:
                    break
                element = stack.pop()
                
            if element[1]>=nums[i]:
                stack.append(element)
            
            stack.append((i,nums[i]))
        # print(stack,index)
        
        for i in range(len(nums)):
            # print(i,stack,sep='-----')
            element = stack.pop()
            while element[1]<nums[i]:
                index[element[0]] = nums[i]
                if not stack:
