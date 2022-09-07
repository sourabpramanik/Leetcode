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
 * @return {string}
 */
var tree2str = function(root) {
    if(!root) return ""
    
    let res = (root.val).toString()
    
    let L = tree2str(root.left)
    let R = tree2str(root.right)
    
    let left = L.toString()
    let right = R.toString()
    
    if(left==="" && right==="") return res
    if(left==="" ) return res + "()" + "(" + right + ")"
    if(right==="" ) return res + "(" + left + ")"
    return res + "(" + left + ")" + "(" + right + ")"
};