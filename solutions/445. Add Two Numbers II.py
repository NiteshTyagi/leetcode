# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_array,l2_array = '',''
        while l1:
            l1_array+=str(l1.val)
            l1 = l1.next
        while l2:
            l2_array+=str(l2.val)
            l2 = l2.next
        result = str(int(l1_array)+int(l2_array))
        
        head = None
        for i in result:
            node =  ListNode(int(i))
            if not head:
                head = node
                ptr = head
            else:
                ptr.next = node
                ptr = ptr.next
        return head
