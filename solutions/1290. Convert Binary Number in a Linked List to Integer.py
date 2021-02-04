# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s_temp = []
        ptr = head
        while ptr:
            s_temp.append(ptr.val)
            ptr = ptr.next
        result=0
        for i in range(len(s_temp)-1,-1,-1):
            result+=(2**i)*(s_temp[len(s_temp)-1-i])
        return result
