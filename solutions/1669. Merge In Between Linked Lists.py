# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        array=[]
        while list1:
            array.append(list1)
            list1 = list1.next
        temp = []
        i= 0 
        
        while i<len(array):
            if a<=i<=b:
                while list2:
                    temp.append(list2)
                    list2=list2.next
                i=b+1
            else:
                temp.append(array[i])
                i+=1
                
        temp[-1].next = None
        for i in range(len(temp)-2,-1,-1):
            temp[i].next = temp[i+1]
            
        return temp[0]
