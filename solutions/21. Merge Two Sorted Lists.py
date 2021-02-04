# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        array=[]
        while (l1 and l2):
            if(l1.val>= l2.val):
                array.append(l2)
                l2 = l2.next
            else:
                array.append(l1)
                l1 = l1.next
        while l1:
            array.append(l1)
            l1 = l1.next
        while l2:
            array.append(l2)
            l2 = l2.next
        if array:
            array[-1].next = None
            for i in range(len(array)-2,-1,-1):
                array[i].next = array[i+1]
            head = array[0]
            return head
        return l1 and l2
        
                
            
        
