# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp=ListNode(0)
        p=tmp
        p.next=head
        
        l=0
        while head:
            l+=1
            head=head.next
        
        for _ in range(0, l-n):
            p=p.next
        
        p.next=p.next.next
        return tmp.next