# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        dummy=ListNode(0)
        
        dummy.next = head        
        prev = dummy  
        cur = dummy
        nex = dummy
        
        while head:
            n+=1
            head=head.next
            
        while n>=k:
            cur=prev.next
            nex=cur.next
            
            for _ in range(1, k):
                cur.next = nex.next
                nex.next = prev.next
                prev.next=nex
                nex=cur.next
            
            prev=cur
            n-=k
        
        return dummy.next
            
        
        