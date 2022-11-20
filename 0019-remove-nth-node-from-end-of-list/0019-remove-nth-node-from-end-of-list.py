# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p=head
        
        k=0
        while p:
            k+=1
            p=p.next
       
        p=dummy
        
        for i in range(0, k-n):
            p=p.next
        
        p.next = p.next.next
        return dummy.next 
        