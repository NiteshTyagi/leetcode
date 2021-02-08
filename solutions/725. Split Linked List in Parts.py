# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        def processed(arr):
            if arr:
                arr[-1].next = None
                for j in range(len(arr)-2,-1,-1):
                    arr[j].next = arr[j+1]
                return arr[0]
            return None
        
        array = []
        while root:
            array.append(root)
            root = root.next
        
        split = len(array)//k
        remaining = len(array)%k
        result = [None]*(k)
        start,end = 0,0
        
        for i in range(k):
            if i<remaining:
                j = split + 1
            else:
                j = split + 0
            start= end
            end = end+j
            result[i]=processed(array[start:end])
        return result
        
                
        
