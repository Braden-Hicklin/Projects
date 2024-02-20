# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        newVal = 0
        carry = 0

        while l1 and l2:
            newVal = l1.val + l2.val + carry
            carry = 0
            if newVal >= 10:
                carry = newVal // 10
                newVal %= 10
            tail.next = ListNode(newVal)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 and not l2:
            newVal = l1.val + carry
            carry = 0
            if newVal >= 10:
                carry = newVal // 10
                newVal %= 10
            tail.next = ListNode(newVal)
            tail = tail.next
            l1 = l1.next
        
        while l2 and not l1:
            newVal = l2.val + carry
            carry = 0
            if newVal >= 10:
                carry = newVal // 10
                newVal %= 10
            tail.next = ListNode(newVal)
            tail = tail.next
            l2 = l2.next
        
        if carry != 0:
            tail.next = ListNode(carry)
            
        return dummy.next