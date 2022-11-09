# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        nodes = {}
        
        for p, c, l in descriptions:
            p_node = nodes.setdefault(p, TreeNode(p))            
            c_node = nodes.setdefault(c, TreeNode(c))
            
            if l:
                p_node.left = c_node
            else:
                p_node.right = c_node
        
            children.add(c)
            
        root = (set(nodes)-set(children)).pop()
        return nodes[root]
            