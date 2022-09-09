# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        fast = head
        slow = head        
        cycle = False
        
        while(fast and fast.next):
            head = head.next            
            fast = fast.next.next
          
            if(fast==head):
                cycle = True
                break
        
        if not cycle: return None
        fast = head
        while fast!=slow:
            slow = slow.next
            fast=fast.next
        return slow
        
        return None