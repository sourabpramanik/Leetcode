# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        
        ds={}
        
        while a:
            ds[a]=1
            a=a.next
        
        while b:
            if b in ds:
                return b
            b=b.next
        
        return None