# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # gets the kth node in group
            kNode = self.getKthNode(groupPrev, k)
            # edgecase for final node
            if not kNode:
                break
            # gets node after the end of group
            groupNext = kNode.next
            
            # reverse
            prev, curr = kNode.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # stores first node in group
            temp = groupPrev.next
            groupPrev.next = kNode
            groupPrev = temp
        
        return dummy.next

    # gets the kth node in group
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr