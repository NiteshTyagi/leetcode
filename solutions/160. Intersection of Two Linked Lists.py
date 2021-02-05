# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        else:
            ptr1 = headA
            ptr2 = headB
            while ptr1!=ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next                
                if(ptr1==ptr2):
                    return ptr1
                if(ptr1==None):
                    ptr1=headB
                if(ptr2==None):
                    ptr2=headA
            return ptr1
        
