# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    temp = None
    maxi = None

    def pairSum(self, head: Optional[ListNode]) -> int:
        self.temp = head
        self.maxi = float("-inf")
        self.rec(head)
        return self.maxi
    
    def rec(self,head):
        if not head:
            return
        self.rec(head.next)
        
        self.maxi = max(self.maxi, self.temp.val+head.val)
        self.temp = self.temp.next
    