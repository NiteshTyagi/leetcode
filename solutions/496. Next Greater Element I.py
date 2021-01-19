class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        for i in nums1:
            if i in nums2:
                index = nums2.index(i)
                filtered= list(filter(lambda x:True if x>i else False,nums2[index+1:]))
                if index<len(nums2)-1 and filtered:
                    stack.append(filtered[0])
                else:
                    stack.append(-1)
        return stack
