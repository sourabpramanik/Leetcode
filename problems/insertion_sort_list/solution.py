# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        while i:
            j = head
            
            while j!=i:
                if j.val > i.val:
                    j.val, i.val = i.val, j.val
                
                j = j.next
            i = i.next
        
        return head
            
            