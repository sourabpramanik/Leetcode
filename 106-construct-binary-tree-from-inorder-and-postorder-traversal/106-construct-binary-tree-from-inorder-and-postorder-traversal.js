/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    if(inorder.length==0 || postorder.length==0){
        return null
    }
    
    let idx = postorder.length-1  
    let pt = inorder.indexOf(postorder[idx])
    let root = new TreeNode(postorder[idx])
    root.left = buildTree(inorder.slice(0, pt), postorder.slice(0, pt))
    root.right = buildTree(inorder.slice(pt+1,inorder.length), postorder.slice(pt, idx))
    
    return root
};