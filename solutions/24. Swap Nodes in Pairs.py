# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ptr = head
        while ptr and ptr.next:
            temp = ptr.val
            ptr.val = ptr.next.val
            ptr.next.val = temp
            ptr = ptr.next.next
        return head
        
