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
            slow=slow.next
            fast=fast.next.next
        
        slow=self.reverse(slow)
        
        p=head
        
        while slow:
            if p.val!=slow.val:
                return False
            slow=slow.next
            p=p.next
        
        return True
    
    def reverse(self, node):
        
        pre=None
        cur=node
        nex=None
        
        while cur:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        
        return pre
        