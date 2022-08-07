# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = dum = ListNode(-1)
        carry = 0
        
        p1 = l1
        p2 = l2
        
        while p1 and p2:
            value = p1.val + p2.val + carry
            mod = value%10
            carry = value//10
            
            dum.next = ListNode(mod)
            dum = dum.next
            
            p1 = p1.next
            p2 = p2.next
        
        if(p1):
            while(p1):
                value = p1.val + carry
                mod = value%10
                carry = value//10
                
                dum.next = ListNode(mod)
                dum = dum.next

                p1 = p1.next
            if(carry!=0):                
                dum.next = ListNode(carry)
        elif(p2):
            while(p2):
                value = p2.val + carry
                mod = value%10
                carry = value//10
                
                dum.next = ListNode(mod)
                dum = dum.next

                p2 = p2.next
            if(carry!=0):
                dum.next = ListNode(carry)
        else:
            if(carry!=0):
                dum.next = ListNode(carry)
        return ret.next
        