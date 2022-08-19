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
                    
        return self.helper(head, None)
    
    def helper(self, head, tail):
        if head==tail:
            return None

        fast = head
        slow = head

        while fast!=tail and fast.next!=tail:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val)
        root.left = self.helper(head, slow)
        root.right = self.helper(slow.next, tail)

        return root
            