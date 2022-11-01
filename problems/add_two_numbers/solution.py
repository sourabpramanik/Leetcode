# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        ans = ListNode(0)
        dum = ans
        carry = 0
        while p1 and p2:
            value = p1.val + p2.val + carry
            mod = value%10
            carry = value//10
            dum.next = ListNode(mod)
            p1 = p1.next
            p2 = p2.next
            dum = dum.next
        
        while p1:
            value = p1.val + carry
            mod = value%10
            carry = value//10
            dum.next = ListNode(mod)
            p1 = p1.next
            dum = dum.next
        
        while p2:
            value = p2.val + carry
            mod = value%10
            carry = value//10
            dum.next = ListNode(mod)
            p2 = p2.next
            dum = dum.next
        if carry!=0:
            dum.next = ListNode(carry)
        return ans.next
            
        