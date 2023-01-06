# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        self.dfs(root, ans, 0)
        return ans[::-1]
    
    def dfs(self, node, arr, lev):
        if not node:
            return
        if lev>=len(arr):
            arr.append([])
        self.dfs(node.left, arr, lev+1)
        self.dfs(node.right, arr, lev+1)
        
        arr[lev].append(node.val)