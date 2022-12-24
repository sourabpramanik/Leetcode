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
        p1=list1
        p2=list2

        if p1.val > p2.val:
            p1, p2 = p2, p1

        res=p1    

        while p1 and p2:
            temp=None
            while p1 and p1.val<=p2.val:
                temp=p1
                p1=p1.next
            temp.next=p2
            p1, p2=p2, p1
        
        return res