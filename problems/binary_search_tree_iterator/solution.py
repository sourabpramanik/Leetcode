# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.addNodes(root)

    def next(self) -> int:
        ans=None
        cur=self.stack.pop()
        ans=cur.val
        self.addNodes(cur.right)
        return ans

    def hasNext(self) -> bool:
        if len(self.stack):
            return True
        return False
    
    def addNodes(self, node):
        while node:
            self.stack.append(node)
            node=node.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()