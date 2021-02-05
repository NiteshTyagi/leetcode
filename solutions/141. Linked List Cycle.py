# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = dict()
        while head:
            if head not in d:
                d[head] = True
            else:
                return True
            head = head.next
        return False
        
