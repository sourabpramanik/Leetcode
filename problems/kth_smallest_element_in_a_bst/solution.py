# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur=root
        counter=0
        ans=-1
        while cur:
            if not cur.left:
                ans=cur.val
                counter+=1
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                
                if not prev.right:
                    prev.right=cur
                    cur=cur.left
                else:
                    prev.right=None
                    ans=cur.val
                    counter+=1
                    cur=cur.right
            if counter==k:
                break
        return ans