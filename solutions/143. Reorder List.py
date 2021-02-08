# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        array = []
        while head:
            array.append(head)
            head = head.next
        result = []
        for i in range(len(array)):
            j = len(array)-i-1
            if i<j:
                result.append(array[i])
                result.append(array[j])
            elif i==j:
                result.append(array[i])
            else:
                break
        if result:
            result[-1].next = None
            for i in range(len(result)-2,-1,-1):
                result[i].next = result[i+1]
            head = result[0]
            
            
        
