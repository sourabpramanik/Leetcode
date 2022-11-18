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
        
        ans=ListNode(0)
        k=ans
        l=list1
        r=list2
        
        while l and r:
            node = ListNode()
            if l.val <= r.val:
                node.val = l.val                
                l=l.next
            else:
                node.val = r.val               
                r=r.next
                
            k.next = node
            k = k.next
        
        if l:
            k.next = l
            k=k.next
        
        if r:
            k.next = r
            k = k.next
        
        return ans.next