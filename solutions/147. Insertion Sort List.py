# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        array = []
        while head:
            array.append(head.val)
            head = head.next
        array.sort()
        head = None
        for i in array:
            node = ListNode(i)
            if not head:
                head = node
                ptr = head
            else:
                ptr.next = node
                ptr = ptr.next
        return head
