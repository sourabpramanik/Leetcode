# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        stack=[]
        cur=root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                temp=stack[-1].right
                if not temp:
                    temp=stack.pop()
                    arr.append(temp.val)
                    while stack and temp==stack[-1].right:
                        temp=stack.pop()
                        arr.append(temp.val)
                else:
                    cur=temp                    
        
        return arr