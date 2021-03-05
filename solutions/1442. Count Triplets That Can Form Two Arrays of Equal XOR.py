class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result=0
        for i in range(len(arr)-1):
            xor = 0
            '''
            We are using Xor property:
            A^(B^C)==(A^B)^C
            '''             
            for j in range(i,len(arr)):
                xor^=arr[j]
                if xor==0:
                    result+=j-i
        return result
        
