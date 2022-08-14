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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if(root===null){
        return root
    }
    
    function helper(node){
        if(node===null) return null
        
        let newTree = new TreeNode(node.val)      
        newTree.left = helper(node.right)
        newTree.right = helper(node.left)
        
        
        return newTree
    }
    
    return helper(root)
};