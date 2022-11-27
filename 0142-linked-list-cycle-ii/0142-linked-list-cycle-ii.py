# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f=head
        s=head
        cycle=False
        while f and f.next:
            f=f.next.next
            s=s.next
            if s==f:
                cycle=True
                break
        
        if cycle:
            p=head
            while p!=s:
                p=p.next
                s=s.next
            
            return s
        
        return None
        