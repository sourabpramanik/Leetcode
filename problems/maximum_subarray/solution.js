/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let max= -Infinity;
    let curr = 0;
    
    for(let num of nums){
        curr += num;
        if(max<curr){
            max = curr;
        } 
        if(curr<0) curr = 0
    }
    return max
};