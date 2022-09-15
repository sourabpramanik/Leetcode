# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, head, root):
        
        if head is None: return True        
        if root is None: return False
        
        if(head.val == root.val):
            return self.util(head.next, root.left) or self.util(head.next, root.right)
        else:
            return False
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None: return False
        if head is None: return True        
        
        
        isP = False
        
        if(head.val == root.val):
            isP = self.util(head.next, root.left) or self.util(head.next, root.right)
        
        return isP or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)