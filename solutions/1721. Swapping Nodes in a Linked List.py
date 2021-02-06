# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        array = []
        while head:
            array.append(head)
            head = head.next
        temp = array[k-1]
        array[k-1] = array[-k]
        array[-k] = temp
        array[-1].next = None
        for i in range(len(array)-2,-1,-1):
            array[i].next = array[i+1]
        
        return array[0]
