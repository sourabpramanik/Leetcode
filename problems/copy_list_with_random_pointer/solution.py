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
            return head
        
        cur=head
        while cur:
            temp=cur.next
            cur.next=Node(cur.val)
            cur.next.next=temp
            cur=temp
        
        cur=head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur=cur.next.next
        
        res=Node(0)
        p=res
        cur=head
        while cur:
            front=cur.next.next
            p.next=cur.next
            p=p.next
            cur.next=front
            cur=cur.next
        
        return res.next