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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    let prev = null
    let first = null
    let last = null
    
    function rec(node){
        if(!node){
            return null
        }
        
        rec(node.left)
        
        if(!first && node.val<prev.val){
            first = prev
        }
        if(first && node.val<prev.val){
            last = node
        }
        
        prev = node
        rec(node.right)
    }
    
    prev = new TreeNode(-Infinity)
    
    rec(root)
    
    let t = first.val
    first.val = last.val
    last.val = t
    
    return root
};