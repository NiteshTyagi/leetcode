class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        def check_arithmetic(arr):
            if len(arr)>1:
                arr.sort()
                diff = arr[1]-arr[0]
                return all([True if arr[i+1]-arr[i]==diff else False for i in range(len(arr)-1)])
            else:
                return False
            
        for i in range(len(l)):
            start = l[i]
            end = r[i]+1
            # print(start,end)
            re = check_arithmetic(nums[start:end])
            result.append(re)
        return result
