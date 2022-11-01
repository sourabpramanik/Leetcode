# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []        
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        
        ans = None
        while stack1 or stack2 or carry:
            f=0
            t=0
            if stack1:
                f = stack1.pop(len(stack1)-1)
            if stack2:
                t = stack2.pop(len(stack2)-1)
            
            value = f+t+carry
            carry = value//10
            mod = value%10
            
            node = ListNode(mod)
            node.next = ans
            ans = node
        
        return ans
            
            
                