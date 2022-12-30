# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        count=0
        maxCount=0
        prev=None
        ans=[]
        cur=root
        while cur:
            if not cur.left:
                if prev==cur.val:
                    count+=1
                else:
                    count=1
                if count==maxCount:
                    ans.append(cur.val)
                elif count>maxCount:
                    ans = [cur.val]
                    maxCount=count
                prev=cur.val
                cur=cur.right
            else:
                temp=cur.left
                while temp.right and temp.right!=cur:
                    temp=temp.right
                if temp.right is None:
                    temp.right=cur
                    cur=cur.left
                else:
                    temp.right=None
                    if prev==cur.val:
                        count+=1
                    else:
                        count=1
                    if count==maxCount:
                        ans.append(cur.val)
                    elif count>maxCount:
                        ans = [cur.val]
                        maxCount=count
                    prev=cur.val
                    cur=cur.right

        return ans

