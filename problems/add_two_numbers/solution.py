# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        p=dummy
        carry=0
        while l1 and l2:
            nodeSum = l1.val + l2.val + carry
            carry = nodeSum//10
            node = ListNode(nodeSum%10)
            p.next = node
            p=p.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            nodeSum = l1.val + carry
            carry = nodeSum//10
            node = ListNode(nodeSum%10)
            p.next = node
            p=p.next
            l1=l1.next
        
        while l2:
            nodeSum = l2.val + carry
            carry = nodeSum//10
            node = ListNode(nodeSum%10)
            p.next = node
            p=p.next
            l2=l2.next
        
        if carry:
            p.next = ListNode(carry)
        
        return dummy.next