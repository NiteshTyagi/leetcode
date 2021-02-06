# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_array = []
        while l1:
            l1_array.append(str(l1.val))
            l1 = l1.next
        
        l2_array = []
        while l2:
            l2_array.append(str(l2.val))
            l2 = l2.next
        
        l1_array = int("".join(l1_array[::-1]))
        l2_array = int("".join(l2_array[::-1]))
        result = str(l1_array+l2_array)[::-1]
        
        head = ListNode(result[0])
        ptr = head
        for r in range(1,len(result)):
            temp = ListNode(result[r])
            ptr.next = temp
            ptr = temp
        return (head)
        
            
        
