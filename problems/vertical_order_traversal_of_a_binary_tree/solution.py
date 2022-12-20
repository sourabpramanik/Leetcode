# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        M=dict()
        stack=[]
        node=root
        v=0
        l=0
        while True:
            if node:
                stack.append((node, v, l))
                node=node.left
                v-=1
                l+=1
            else:
                if not stack:
                    break
                
                node, v, l = stack.pop()
                if not v in M:
                    M[v] = dict()

                if not l in M[v]:
                        M[v][l] = list()
                
                M[v][l].append(node.val)
                
                if len(M[v][l])>1:
                    M[v][l].sort()

                node = node.right
                v+=1
                l+=1
                
        ans=[]
        for key in sorted(M):
            obj = M[key]
            val = []
            for key in sorted(obj):
                arr=obj[key]
                val+=arr
           
            ans.append(val)

        return ans
