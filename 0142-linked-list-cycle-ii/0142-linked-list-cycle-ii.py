# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        p=head
        while fast and fast.next:
            
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                while slow!=p:
                    p=p.next
                    slow=slow.next
                
                return slow
        return None
        
        return None