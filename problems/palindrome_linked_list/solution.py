# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    temp=None
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.temp = head
        return self.rec(head)
        
    def rec(self, head):
        if not head:
            return
        self.rec(head.next)
        
        if(self.temp.val!=head.val):
            return False
        if(self.temp.next==None):
            return True
        self.temp = self.temp.next        