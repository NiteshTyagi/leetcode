# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        
        array_val = []
        while head:
            array_val.append(head.val)
            head = head.next
        stack = [(0,array_val[0])]
        temp = [None]*(len(array_val))
        
        for i in range(1,len(array_val)):
            next_element = array_val[i]
            pop_element = stack.pop()
            while next_element>pop_element[1]:
                temp[pop_element[0]]=next_element
                if not stack:
                    break
                pop_element = stack.pop()
            if next_element<=pop_element[1]:
                stack.append(pop_element)
            stack.append((i,next_element))
            
        while stack:
            pop_element = stack.pop()
            temp[pop_element[0]] = 0
        return temp
        
