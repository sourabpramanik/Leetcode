# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], l: int) -> Optional[ListNode]:
        n=0
        dummy=ListNode(0)
        p=dummy
        p.next=head
        
        while head:
            n+=1
            head=head.next
        
        for _ in range(0, n-l):
            p=p.next
        
        p.next=p.next.next
        
        return dummy.next