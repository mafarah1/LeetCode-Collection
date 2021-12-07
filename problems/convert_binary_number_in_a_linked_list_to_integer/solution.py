# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        number = ""
        
        while head.next != None:
            number += str(head.val)
            head = head.next
        
        number += str(head.val)
        
        return eval("0b"+number)