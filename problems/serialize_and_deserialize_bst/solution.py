# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        
        def recur(node):
           
            if node:
                vals.append(node.val)                
                recur(node.left)
                recur(node.right)
        
        recur(root)
       
    
        return " ".join(map(str, vals))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        queue = collections.deque(int(val) for val in data.split())     
        def build(minVal, maxVal):
            if queue and minVal<queue[0]<maxVal:
                
                val = queue.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                
                return node
        
        
        
        return build(float("-inf"), float("inf"))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans