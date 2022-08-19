# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        hashMap = {}
        ans = []
        def recur(node, path):
            if node is None:
                return "none"
            
            path += ",".join([str(node.val), recur(node.left, path), recur(node.right, path)])
            
            if path in hashMap:
                hashMap[path] += 1
                if hashMap[path] == 2:
                    ans.append(node)
            else:
                hashMap[path] = 1
                
            
            return path
        
        recur(root, " ")
        # print(ans)
        
        return ans