# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        length=1
        while curr.next:
            length+=1
            curr=curr.next
        
        curr.next=head
        k=k%length
        end=length-k

        while end:
            curr=curr.next
            end-=1
        
        head=curr.next
        curr.next=None

        return head
        

