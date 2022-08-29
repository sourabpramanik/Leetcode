/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let prod1=nums[0], prod2=nums[0], res=nums[0]
    
    for(let i=1; i<nums.length; i++){
        let temp=Math.max(nums[i], Math.max(prod1*nums[i], prod2*nums[i]))
        prod2=Math.min(nums[i], Math.min(prod1*nums[i], prod2*nums[i]))
        prod1=temp   
        
        res=Math.max(res, prod1)
    }
    
    return res
};