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
        store={}
        
        cur=head
        while cur:
            store[cur]=Node(cur.val)
            cur=cur.next
        
        cur=head
        while cur:
            if cur.next:
                store[cur].next = store[cur.next]
            if cur.random:
                store[cur].random = store[cur.random]
            cur=cur.next
        
        return store[head]
        
        