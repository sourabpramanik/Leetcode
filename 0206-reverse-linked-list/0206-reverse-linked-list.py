# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head=head.next
        
        arr = arr[::-1]
        ans = ListNode()
        p=ans
        for val in arr:
            node = ListNode(val)
            p.next = node
            p = p.next
        
        return ans.next