"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        while curr:
            temp=curr.next
            curr.next=Node(curr.val, None, None)
            curr.next.next=temp
            curr=curr.next.next
        
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next
        
        ans=Node(0)
        ptr=ans
        
        curr=head
       
        
        while curr:
            front=curr.next.next
            ptr.next=curr.next
            curr.next=front
            curr=curr.next
            ptr=ptr.next
        
        return ans.next
            