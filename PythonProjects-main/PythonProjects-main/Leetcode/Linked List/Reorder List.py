# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find half way point
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # Seperate linked list into second list at halfway point then reverse
        second = s.next
        prev = s.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge two lists
        dummy = ListNode()
        tail = dummy
        while head and prev:
            tail.next = head
            head = head.next
            tail.next.next = prev
            prev = prev.next
            tail = tail.next.next
        if head and not prev:
            tail.next = head
        elif not head and prev:
            tail.next = prev
        
        # Update original list
        head = dummy.next