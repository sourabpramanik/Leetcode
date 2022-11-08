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
        arr = []
        if not head:
            return None
        pt = head
        while pt:
            arr.append(pt.val)
            pt = pt.next
        
        arr.sort()
        return self.build(arr)
    
    def build(self,arr):
        if len(arr)==0:
            return None
        
        mid = len(arr)//2
        
        root = TreeNode(arr[mid])
        root.left = self.build(arr[:mid])
        root.right = self.build(arr[mid+1:])
        
        return root