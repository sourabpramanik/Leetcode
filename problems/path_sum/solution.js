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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    
    const rec = (node, rem) => {
       
        if(!node){
            return false
        }
        if(!node.left && !node.right && rem-node.val===0){
            return true
        }                
        
        return rec(node.left, rem-node.val) || rec(node.right, rem-node.val)
    }    
    return rec(root, targetSum)
};