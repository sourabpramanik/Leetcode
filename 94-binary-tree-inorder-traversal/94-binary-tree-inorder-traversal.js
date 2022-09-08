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
    let ans = []
    let curr = root
    
    while(curr){
        if(!curr.left){
            ans.push(curr.val)
            curr = curr.right
        }else{
            let temp = curr.left
            while(temp.right && temp.right!==curr){
                temp = temp.right
            }
            if(temp.right===null){
                temp.right=curr
                curr = curr.left
            }else{
                temp.right = null
                ans.push(curr.val)
                curr = curr.right
            }
        }
    }
    
    return ans
    
};