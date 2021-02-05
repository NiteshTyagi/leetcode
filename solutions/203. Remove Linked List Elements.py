# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        array = []
        while head:
            if head.val!=val:
                array.append(head)
            head = head.next
        if array:
            array[-1].next = None
            for i in range(len(array)-2,-1,-1):
                array[i].next = array[i+1]
            return array[0]
        return None
