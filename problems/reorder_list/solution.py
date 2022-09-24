# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    temp = None
    stop = None
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """                
        self.temp = head
        self.stop = False
        self.rec(head)
        
    def rec(self,head):
        if not head: return
        
        self.rec(head.next)
        
        if not self.stop:
            t = self.temp.next
            self.temp.next = head
            head.next = t
            self.temp = t
        
        if self.temp and self.temp.next==head:
            self.temp.next = None
            self.stop = True

        
        