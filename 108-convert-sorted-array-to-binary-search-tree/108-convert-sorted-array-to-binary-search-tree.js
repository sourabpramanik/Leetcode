/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    const build = (nums) => {
        let totalNode =nums.length
    
        if(!totalNode){
            return null
        }

        let mid = Math.floor(totalNode/2)
        let root = new TreeNode(nums[mid])
        root.left = build(nums.slice(0, mid))
        root.right = build(nums.slice(mid+1, totalNode))
        
        return root
    }
    return build(nums)
};