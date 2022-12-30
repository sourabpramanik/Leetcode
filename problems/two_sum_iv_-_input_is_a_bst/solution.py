# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Iterator:
    def __init__(self, root, flag):
        self.stack=[]
        self.left=flag
        self.pushNode(root)
    
    def next(self):
        cur=self.stack.pop()

        if self.left:
            self.pushNode(cur.right)
        else:
            self.pushNode(cur.left)

        return cur.val 

    def pushNode(self, node):
        while node:
            self.stack.append(node)
            if self.left:
                node=node.left
            else:
                node=node.right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left= Iterator(root, True)
        right= Iterator(root, False)

        i=left.next()
        j=right.next()

        while i<j:
            if i+j==k:
                return True
            elif i+j>k:
                j=right.next()
            else:
                i=left.next()
        return False

        