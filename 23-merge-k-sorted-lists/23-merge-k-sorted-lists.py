# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        interval=1
        while interval<len(lists):
            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = self.merger(lists[i], lists[i+interval])
            interval*=2
        
        return lists[0] if len(lists) > 0 else None
        
    def merger(self, l1, l2):
        
        c1 = l1
        c2 = l2
        ln = ListNode(0)
        p = ln
        while c1 and c2:
            node = ListNode()
            if c1.val<=c2.val:
                node.val = c1.val
                node.next = None
                p.next = node
                c1 = c1.next
            else:
                node.val = c2.val
                node.next = None
                p.next = node
                c2 = c2.next
            p = p.next
        
        if c1:
            p.next = c1
        
        if c2:
            p.next = c2
            
        return ln.next
                