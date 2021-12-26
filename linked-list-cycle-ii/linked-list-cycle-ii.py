# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def find_cycle_start(head):
  turtoise = head.next
  hare = head.next.next

  while hare != None and hare.next != None:
    if turtoise == hare:
      cycle_length = calculate_cycle_length(turtoise)
      return find_start(head, cycle_length)
    else:
      turtoise = turtoise.next
      hare = hare.next.next
  
  return None


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length


def find_start(head, cycle_length):
  pointer1 = head
  pointer2 = head
  # move pointer2 ahead 'cycle_length' nodes
  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
          return None
        if head.next == None:
          return None
        return find_cycle_start(head)