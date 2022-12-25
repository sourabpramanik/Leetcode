# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        p=res
        carry=0
        while l1 and l2:
            value1=l1.val
            value2=l2.val
            value=(value1+value2+carry)%10
            carry=(value1+value2+carry)//10
            p.next=ListNode(value)
            p=p.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            value=(l1.val+carry)%10
            carry=(l1.val+carry)//10
            p.next=ListNode(value)
            p=p.next
            l1=l1.next
        
        while l2:
            value=(l2.val+carry)%10
            carry=(l2.val+carry)//10
            p.next=ListNode(value)
            p=p.next
            l2=l2.next
        
        if carry:
            p.next=ListNode(carry)
        
        return res.next