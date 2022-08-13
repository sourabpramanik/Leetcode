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
var maxDepth = function(root) {
    
    if(!root){
        return 0
    }
    
    let stk = [root]
    let lev = 0
    let max = 1
    
    while(stk.length>0){
        curr = stk.shift()
        max--
        if(curr.left){
            stk.push(curr.left)
        }
        if(curr.right){
            stk.push(curr.right)
        }
        if(max==0){
            lev++
            max = stk.length
        }        
    }
    
    return lev
};