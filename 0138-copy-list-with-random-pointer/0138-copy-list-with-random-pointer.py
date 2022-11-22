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
        ds={}
        temp=head
        while temp:
            ds[temp]=Node(temp.val, None, None)
            temp=temp.next
        
        temp=head
        while temp:
            if temp.next:
                ds[temp].next = ds[temp.next]
            if temp.random:
                ds[temp].random = ds[temp.random]
            temp=temp.next
        
        return ds[head]
            