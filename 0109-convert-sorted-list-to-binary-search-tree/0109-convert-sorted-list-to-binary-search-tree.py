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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None        
        
        if not head.next:
            return TreeNode(head.val)
        
        slow, fast = head, head.next.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        node = slow.next
        slow.next = None
        
        root = TreeNode(node.val)
        root.left = self.sortedListToBST(head)        
        root.right = self.sortedListToBST(node.next)
        
        return root