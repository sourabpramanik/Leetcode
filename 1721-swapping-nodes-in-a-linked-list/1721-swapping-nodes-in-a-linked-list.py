# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        fast = head
        slow = head
        
        for _ in range(1, k):
            fast = fast.next
        f=fast
        while fast.next:
            fast=fast.next
            slow=slow.next
        s=slow
        s.val, f.val= f.val, s.val
        
        return head
        
        