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
        
        l1 = list1
        l2 = list2
        
        if l1.val>l2.val:
            l1, l2 = l2, l1
        
        res=l1
        
        while l1 and l2:
            temp = None
            
            while l1 and l1.val<=l2.val:
                temp = l1
                l1 = l1.next
            
            temp.next = l2
            l1, l2 = l2, l1
        
        return res
            
    
    def swap(self, l1, l2):
        l1, l2 = l2, l1