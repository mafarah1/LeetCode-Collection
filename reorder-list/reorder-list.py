# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
  prev = None
  while head != None:
    temp = head.next
    head.next = prev
    prev = head
    head = temp
  return prev

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      fast,slow = head,head

      while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next

      middle = reverse(slow)
      copy_middle = middle

      while middle != None and head != None:
        temp = head.next
        head.next = middle
        head = temp

        temp = middle.next
        middle.next = head
        middle = temp

      # set the next of the last node to 'None'
      if head is not None:
        head.next = None
        