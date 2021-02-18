class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = dict()
        result = []
        for i in nums:
            count = nums.count(i)
            if count not in d:
                d[count]=[i]
            else:
                d[count].append(i)
        for key,value in sorted(d.items(),key=lambda x:x[0]):
            result.extend(sorted(value,reverse=True))
        return result
    
