# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        p = head
        
        while p:
            if not p.next: return head
            q = p.next
            p.val, q.val = q.val, p.val
            p = q.next            
            
        return head