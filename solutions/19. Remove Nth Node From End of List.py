# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        array=[]
        while head:
            array.append(head)
            head = head.next
        index = len(array)-n
        array.pop(index)
        if array:
            array[-1].next=None
            for i in range(len(array)-2,-1,-1):
                array[i].next = array[i+1]
            return array[0]
        return None
        print(array)
        
