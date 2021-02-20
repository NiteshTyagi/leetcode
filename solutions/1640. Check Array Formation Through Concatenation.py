class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = 0
        new_index = index
        while index<len(arr):
            curr = arr[index]
            for a in pieces:
                if a[0]==curr and a==arr[index:index+len(a)]:
                    new_index = index+len(a)
                    pieces.remove(a)
            if new_index==index:
                return False
            else:
                index = new_index
        return True
        
