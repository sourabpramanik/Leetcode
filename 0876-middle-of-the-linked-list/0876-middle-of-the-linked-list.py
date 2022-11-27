# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        p=head
        while p:
            count+=1
            p=p.next
        
        mid=head
        for _ in range(0,count//2):
            mid=mid.next
        
        return mid