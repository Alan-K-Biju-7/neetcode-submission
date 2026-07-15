# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      temp = head
      N = 0
      while temp:
        temp = temp.next
        N += 1
      if n == N:
            return head.next  
      count1 = N - n - 1
      temp1 = head
      for i in range(count1):
        temp1 = temp1.next
      temp1.next = temp1.next.next
      return head

        