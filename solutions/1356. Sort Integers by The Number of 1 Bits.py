class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        def check_binary(elem):
            return bin(elem).count('1')
        
        arr.sort(key=check_binary)
        return arr
        
        
