# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pre=None
        curr=head
        nex=None
        
        while curr:
            nex= curr.next
            curr.next=pre
            pre=curr
            curr = nex
        
        return pre