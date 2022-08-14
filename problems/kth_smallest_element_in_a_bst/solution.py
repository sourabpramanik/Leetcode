# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        curr = root
        counter = 0
        while curr is not None:
            
            if curr.left is None:
                ans.append(curr.val)
                counter+=1
                curr = curr.right
            else:
                temp = curr.left
                
                while temp.right and temp.right!=curr:
                    temp = temp.right
                    
                if temp.right is None:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right=None
                    ans.append(curr.val)
                    counter+=1
                    curr = curr.right
            if k==counter: break 
        
        return ans.pop()

        
        