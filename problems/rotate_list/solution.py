# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n=1
        cur=head
        while cur.next:
            n+=1
            cur=cur.next
            
        cur.next=head
        
        k=k%n
        end=n-k
        while end:
            cur=cur.next
            end-=1
        
        head=cur.next  
        cur.next=None
        
        return head
        