# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head
        
        count=0
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy        
        prev=dummy        
        nex=dummy
        
        while curr.next:
            count+=1
            curr = curr.next
        
        while count>=k:
            curr=prev.next            
            nex=curr.next
            
            for i in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            
            prev=curr
            count-=k
        
        return dummy.next