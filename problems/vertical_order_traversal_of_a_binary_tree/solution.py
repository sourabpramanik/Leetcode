# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = dict()
        queue=collections.deque([(root, 0, 0)])
        while queue:
            size=len(queue)
            while size:
                node, ver, lev = queue.popleft()
                if node:
                    if not ver in store:
                        store[ver] = dict()
                    if not lev in store[ver]:
                        store[ver][lev]=list()
                    store[ver][lev].append(node.val)
                    store[ver][lev].sort()
                    if node.left:
                        queue.append((node.left, ver-1, lev+1))
                    if node.right:
                        queue.append((node.right, ver+1, lev+1))
                size-=1
        
        ans=[]
        for key in sorted(store):
            temp=[]
            for arr in store[key].values():
                temp+=arr
            ans.append(temp[:])
        return ans
