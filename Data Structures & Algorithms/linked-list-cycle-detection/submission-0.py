# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = ListNode()
        current = head
        seenNodes = []
        while current is not None:
            if current.next in seenNodes:
                return True
            seenNodes.append(current)
            current = current.next

        return False