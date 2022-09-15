# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ans = ListNode(0)
        
        p = head        
        q = ans 
        r=head
        
        while p:
            n = ListNode()
            if p.val<x:
                n.val = p.val
                n.next = None
                q.next = n
                q = q.next
            p = p.next
            
        while r:
            n = ListNode()
            if r.val>=x:
                n.val = r.val
                n.next = None
                q.next = n
                q = q.next
            r = r.next
            
        return ans.next
            