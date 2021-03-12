class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0]*32
        for i in range(32):
            for num in nums:
                if(abs(num)&(1<<i)!=0):
                    count[i]+=1     
        res = 0
        for c in range(32):
            if count[c]%3!=0:
                res+= (count[c]%3)*(1<<c)
        if nums.count(res)==1:
            return res
        else:
            return -res
​
        
            
