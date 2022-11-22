# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n=1
        temp=head
        while temp.next:
            n+=1
            temp=temp.next
        
        temp.next=head
        k=k%n
        end=n-k
        while end:
            temp=temp.next
            end-=1
        
        head=temp.next
        temp.next=None
        
        return head
        