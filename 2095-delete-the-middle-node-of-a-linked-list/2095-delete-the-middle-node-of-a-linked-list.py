# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head.next
        s = f = head
        pre = None
        while f and f.next:
            
            f = f.next.next
            pre = s
            s = s.next
        
        pre.next = s.next
        s.next = None
        
        return head
        