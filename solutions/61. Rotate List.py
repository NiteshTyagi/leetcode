# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        array = []
        while head:
            array.append(head)
            head = head.next
        
        k = k%len(array)
        for i in range(k):
            last_element = array.pop()
            array.insert(0,last_element)
            
        array[-1].next = None
        for i in range(len(array)-2,-1,-1):
            array[i].next = array[i+1]
        return array[0]
        
               
