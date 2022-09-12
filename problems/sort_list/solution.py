# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next  
        
        prev.next = None
        L = self.sortList(head)
        R = self.sortList(slow)
        
        return self.mergeList(L, R)
    
    def mergeList(self, list1, list2):
        curr1 = list1        
        curr2 = list2
        mergeList = ListNode(0)
        ptr = mergeList
        
        while curr1 and curr2:

            if not curr2 or curr1.val <= curr2.val:                               
                ptr.next = curr1
                curr1 = curr1.next
                ptr = ptr.next
            else:               
                ptr.next = curr2
                curr2 = curr2.next
                ptr = ptr.next        
        
        if curr1:
            ptr.next = curr1
            
        if curr2:
            ptr.next = curr2
        
        return mergeList.next