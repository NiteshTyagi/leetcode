class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        # print(arr)
        diff = set([arr[i+1]-arr[i] for i in range(len(arr)-1)])
        # print(diff)
        if len(diff)==1:
            return True
        else:
            return False
        
