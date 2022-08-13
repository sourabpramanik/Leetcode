/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    
    
    function rec(node){
        if (node===null){
            return null
        }
        let lh = rec(node.left) 
        let rh = rec(node.right)
            
        if(node.left===null || node.right===null){
            return 1+ Math.max(lh,rh)
        }
        return 1+ Math.min(lh,rh)
    }
    return rec(root)
    
};