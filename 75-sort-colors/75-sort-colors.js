/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for(let i=1; i<nums.length; i++){
        let curr = nums[i];
        
        let j=i-1;
        
        while(j>-1 && curr < nums[j]){
            nums[j+1] = nums[j]
            j--;
        }
        nums[j+1] = curr;
    }
        
};