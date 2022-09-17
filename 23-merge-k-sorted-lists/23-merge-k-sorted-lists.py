# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.partition(lists, 0, len(lists)-1)
    
    def partition(self, arr, s, e):
        if s==e:
            return arr[s]
        
        if s<e:
            q = (s+e)//2
            L = self.partition(arr, s, q)            
            R = self.partition(arr, q+1, e)
            return self.merger(L, R)
        else:
            return None
        
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
                