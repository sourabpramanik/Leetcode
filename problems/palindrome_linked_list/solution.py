# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        mid=self.getMid(head)
        slow=head
        while mid:
            slow=slow.next
            mid-=1
        
        slow=self.reverse(slow)
        p=head

        while slow:
            if slow.val!=p.val:
                return False
            slow=slow.next
            p=p.next
        
        return True

    def getMid(self, head):
        mid=0
        fast=head
        while fast and fast.next:
            mid+=1
            fast=fast.next.next
        
        return mid
    
    def reverse(self, head):
        prev=None
        cur=head

        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        
        return prev