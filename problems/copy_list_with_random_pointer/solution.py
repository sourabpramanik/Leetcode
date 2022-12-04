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
            tmp=cur.next
            cur.next = Node(cur.val)
            cur.next.next=tmp
            cur=cur.next.next
        
        cur=head
        while cur:            
            if cur.random:
                cur.next.random = cur.random.next
            cur=cur.next.next
        
        ans=Node(0)
        p=ans
        cur=head
        while cur:
            front=cur.next.next
            p.next=cur.next
            cur.next=front
            cur = cur.next
            p=p.next
        
        return ans.next
        
        