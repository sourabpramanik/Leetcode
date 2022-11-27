# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        p=dummy
        p.next=head
        f=dummy
        s=dummy
    
        for _ in range(0, n):
            f=f.next
        
        while f and f.next:
            f=f.next
            s=s.next
        
        s.next = s.next.next
        return dummy.next