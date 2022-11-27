# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        
        p=list1
        q=list2
        if p.val>q.val:
            p, q = q, p
            
        res=p
        
        while p and q:
            temp=None
            while p and p.val<=q.val:
                temp=p
                p=p.next
            
            temp.next=q
            p, q = q, p
        
        return res