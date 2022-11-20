# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        ptr=head
        
        while ptr:
            n+=1
            ptr = ptr.next
        
        ptr=head
        
        i=0
        while i<n//2:
            ptr = ptr.next
            i+=1
        return ptr