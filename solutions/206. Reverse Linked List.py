# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        array=[]
        while head:
            array.append(head)
            head = head.next
        if array:
            array = array[::-1]
            array[-1].next=None
            for i in range(len(array)-2,-1,-1):
                array[i].next = array[i+1]
            head = array[0]
        return head
