# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr1=[]
        arr2=[]

        self.dfs(root, arr1, p)
        self.dfs(root, arr2, q)

        i=0
        j=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i].val!=arr2[j].val:
                break
            i+=1
            j+=1
        
        return arr1[i-1]

    def dfs(self, node, arr, target):
        if not node:
            return
        
        arr.append(node)
        if node.val==target.val:
            return True
        l=self.dfs(node.left, arr,target)
        r=self.dfs(node.right, arr, target)

        if l or r:
            return True
        arr.pop()
        return False