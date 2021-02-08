# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        array = []
        while head:
            array.append(head)
            head = head.next
        m = m-1
        i=0
        result = []
        while (i<len(array)):
            if i==m:
                result.extend(list(reversed(array[m:n])))
                i=n
            else:
                result.append(array[i])
                i+=1
        if result:
            result[-1].next = None
            for i in range(len(result)-2,-1,-1):
                result[i].next = result[i+1]
            return result[0]
        
        
        
        
