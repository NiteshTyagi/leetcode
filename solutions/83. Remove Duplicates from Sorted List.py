# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev_element=head
        ptr = head.next
        while ptr:
            if ptr.val==prev_element.val:
                prev_element.next = ptr.next
            else:
                prev_element = prev_element.next
            ptr = ptr.next
        return head
        
