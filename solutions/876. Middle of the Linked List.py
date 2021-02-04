# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if(head.next==None):
            return head
        elif(head.next.next==None):
            return head.next
        else:
            count_len = 0
            ptr=head
            while ptr:
                count_len+=1
                ptr = ptr.next
            index = (count_len)//2
            
            while head and index:
                index-=1
                head = head.next
            return head
        
        
