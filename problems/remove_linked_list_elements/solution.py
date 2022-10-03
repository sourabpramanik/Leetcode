# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        
        def rec(prev, curr):
            if not curr:
                return None
            
            if curr.val==val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            rec(prev, curr)
        
        rec(dummy, head)
        
        return dummy.next
            
            