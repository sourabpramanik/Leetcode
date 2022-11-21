# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ds={}
        p=head
        while p:
            if p in ds:
                return p
            
            ds[p]=1
            p=p.next
        
        return None