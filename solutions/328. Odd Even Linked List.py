# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        count = 1
        odd,even=[],[]
        
        while head:
            if (count%2)!=0:
                odd.append(head)
            else:
                even.append(head)
            count+=1
            head = head.next
        odd.extend(even)
        odd[-1].next = None
        for i in range(len(odd)-2,-1,-1):
            odd[i].next = odd[i+1]
        return odd[0]
                
        
