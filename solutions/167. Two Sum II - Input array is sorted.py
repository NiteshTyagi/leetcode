class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary_search(A,l,r,key):
            index=-1
            while(l<=r):
                mid=(l+r)//2
                if A[mid]==key:
                    index=mid
                    break
                elif A[mid]<key:
                    l=mid+1
                else:
                    r=mid-1
            return index
        
        count=1
        for i in range(len(numbers)):
            count+=1
            key = target - numbers[i]
            index = binary_search(numbers[i+1:],0,len(numbers[i+1:])-1,key)
            if index==-1:
                continue
            else:
                return [i+1,index+count]
        
