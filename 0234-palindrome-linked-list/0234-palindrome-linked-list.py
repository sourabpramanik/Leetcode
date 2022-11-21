# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        slow = self.reverse(slow)
        d=head
        while slow:
            if slow.val!= d.val:
                return False
            d=d.next
            slow=slow.next
        
        return True
        
    def reverse(self, node):
        pre=None
        curr=node
        nex=None
        
        while curr:
            nex=curr.next
            curr.next=pre
            pre=curr
            curr=nex
        
        return pre