# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev_node = None
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                if len(stack)!=0:
                    root = stack.pop()
                    if prev_node !=None and prev_node >= root.val:
                        return False

                    prev_node = root.val
                    root = root.right
        
        return True