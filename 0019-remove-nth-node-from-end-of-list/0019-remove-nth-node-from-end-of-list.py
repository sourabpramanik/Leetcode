# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        dummy = ListNode(0)
        ptr = dummy
        ptr.next=head
        
        while head:
            i+=1
            head = head.next
                
        for _ in range(0, i-n):
            ptr = ptr.next
        
        ptr.next = ptr.next.next
        
        return dummy.next