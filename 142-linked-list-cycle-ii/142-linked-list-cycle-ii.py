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
        while(fast and fast.next):
            head = head.next            
            fast = fast.next.next
          
            if(fast==head):
                
                while head!=slow:
                    slow = slow.next
                    head=head.next
                return slow
        
        return None