class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        i,e,o=0,0,0
        result = []
        while(i<len(A)):
            if(i%2==0):
                result.append(even[e])
                e+=1
            else:
                result.append(odd[o])
                o+=1
            i+=1
        return result
