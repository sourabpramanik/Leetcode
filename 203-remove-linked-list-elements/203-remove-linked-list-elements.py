# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        
        def rec(curr):
            if not curr.next:
                return None
            
            if curr.next.val==val:
                curr.next = curr.next.next
            else:
                curr = curr.next
            rec(curr)
        
        rec(dummy)
        
        return dummy.next
            
            