# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        dummy=ListNode()
        dummy.next=head
        cur=dummy
        while cur:
            cur=cur.next
            count+=1
        
        prev=dummy

        while count>k:
            cur=prev.next
            nex=cur.next

            for _ in range(1, k):
                cur.next=nex.next
                nex.next=prev.next
                prev.next=nex
                nex=cur.next
            prev=cur
            count-=k
        
        return dummy.next
        
