"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue=collections.deque([root])

        while queue:
            prev=None
            size=len(queue)
            for _ in range(0, size):
                node=queue.popleft()
                if node:
                    if prev:
                        prev.next = node
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    prev=node

        return root 
