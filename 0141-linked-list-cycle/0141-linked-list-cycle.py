# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store={}
        
        p=head
        
        while p:
            if p in store:
                return True
            store[p] = 1
            p=p.next
        
        return False