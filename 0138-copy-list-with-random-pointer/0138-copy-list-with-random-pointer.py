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
        hashMap={}
        
        node=head
        
        while node:
            hashMap[node] = Node(node.val)
            node=node.next
        
        for node in hashMap:
            if node.next in hashMap:
                hashMap[node].next = hashMap[node.next]
            if node.random in hashMap:
                hashMap[node].random = hashMap[node.random]
        
        return hashMap[head]
                