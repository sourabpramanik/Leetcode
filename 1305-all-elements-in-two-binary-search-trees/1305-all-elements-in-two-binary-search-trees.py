# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree = []
        
        
        self.preOrder(root1, tree)
        self.preOrder(root2, tree)
        
        return self.mergeSort(tree)
    
    def preOrder(self, node, arr):
        if not node:
            return None
        
        arr.append(node.val)
        self.preOrder(node.left, arr)
        self.preOrder(node.right, arr)
                
    
    def mergeSort(self, arr):
        if len(arr)>1:            
        
            mid = len(arr)//2

            L = self.mergeSort(arr[:mid])
            R = self.mergeSort(arr[mid:])


            i=0
            j=0
            k=0

            while i<len(L) and j<len(R):

                if L[i]<=R[j]:
                    arr[k] = L[i]
                    i+=1
                    k+=1
                else:
                    arr[k] = R[j]
                    j+=1
                    k+=1

            while i<len(L):
                arr[k] = L[i]
                i+=1
                k+=1

            while j<len(R):
                arr[k] = R[j]
                j+=1
                k+=1
            
        return arr