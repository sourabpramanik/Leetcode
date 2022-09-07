# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.help(head, None)
    
    def help(self, curr, prev):
        if not curr: return prev
        
        n = curr.next
        curr.next=prev
        prev=curr
        
        return self.help(n, prev)