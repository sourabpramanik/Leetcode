# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = preR = preL = ListNode(0, head)
        left=right=head
        
        for _ in range(1, k):
            preL=left
            left = left.next
        nc=left
        while nc.next:
            nc=nc.next
            preR=right
            right=right.next
        
        
        preR.next, preL.next = left, right
        left.next, right.next = right.next, left.next
        return dummy.next
        
        