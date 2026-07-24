# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        m = count - n
        current = head
        prev = None
        if m == 0:
            return head.next
        while m > 0:
            prev = current
            current = current.next
            m-=1
        prev.next = current.next
        return head
