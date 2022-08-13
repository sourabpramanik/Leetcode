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
 * @return {boolean}
 */
var isBalanced = function(root) {
    const rec = (root) => {
        if(root===null){
            return 0
        }

        let lh = rec(root.left)
        if(lh===-1) return -1

        let rh = rec(root.right)    
        if(rh===-1) return -1

        if(Math.abs(lh-rh)>1) return -1

        return 1 + Math.max(lh, rh)
    }
    
    return rec(root)!==-1
};
