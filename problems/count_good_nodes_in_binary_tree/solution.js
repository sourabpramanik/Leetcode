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
var goodNodes = function(root) {
    let count=0
    
    function pre(node, max){
        if(!node) return null
        
        if(node.val>=max){
            max=node.val
            count++
        }
        pre(node.left, max)
        pre(node.right, max)
    }
    
    pre(root, -Infinity)
    
    return count
};