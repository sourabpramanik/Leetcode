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
        
        node=head
        
        while node:
            tmp=node.next
            node.next = Node(node.val)
            node.next.next=tmp
            node = node.next.next
        
        node=head
        
        while node:
            if node.random:
                node.next.random = node.random.next
            node=node.next.next
        
        prime=Node(0)
        p=prime
        node=head
        while node:
            front = node.next.next
            p.next = node.next
            node.next = front
            node = node.next
            p=p.next
        
        return prime.next
        
                