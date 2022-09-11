# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if(not head or k==0):
            return head
        
        p = head
        l = 1
        while(p.next):
            p = p.next
            l+=1
         
       
        p.next = head
        
        k = k%l
        
        for i in range(l-k):
            p = p.next
        
        head = p.next
        p.next = None
        
        return head
                