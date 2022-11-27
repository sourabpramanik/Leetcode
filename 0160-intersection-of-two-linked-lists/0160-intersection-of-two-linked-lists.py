# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p=headA
        q=headB
        
        hashMap={}
        while p:
            hashMap[p]=1
            p=p.next
        
        while q:
            if q in hashMap:
                return q
            q=q.next
        
        return None