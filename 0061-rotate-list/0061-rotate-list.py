# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        tmp=head
        n=0
        
        while tmp.next:
            tmp=tmp.next
            n+=1
        n+=1
        tmp.next=head
        k=k%n
        
        end=n-k
        
        while end:
            tmp = tmp.next
            end-=1
        
        head=tmp.next
        tmp.next=None
        
        return head
        
        
        