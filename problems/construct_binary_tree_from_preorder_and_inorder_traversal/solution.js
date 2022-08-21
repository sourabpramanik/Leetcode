/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if(preorder.length==0 || inorder.length==0){
        return null
    }
    
    let root = new TreeNode(preorder[0])
    let pt = inorder.indexOf(preorder[0])
    root.left = buildTree(preorder.slice(1,pt+1), inorder.slice(0, pt))
    root.right = buildTree(preorder.slice(pt+1,preorder.length), inorder.slice(pt+1,inorder.length))
    
    return root
    
    
    
    
    
    
};