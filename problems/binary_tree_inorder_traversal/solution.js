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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let arr = []
    let stack = []
    let current = root
    while(current || stack.length>0){
        while(current){
            stack.push(current)
            current = current.left
        }
        current = stack.pop()
        arr.push(current.val)
        current = current.right
    }
    
  
    return arr
    
};