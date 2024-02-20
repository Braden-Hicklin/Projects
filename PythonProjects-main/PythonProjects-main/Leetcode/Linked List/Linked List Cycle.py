# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        old = {}

        while head:
            old[head] = head
            if head.next in old:
                return True
            head = head.next
        return False