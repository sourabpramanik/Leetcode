/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let l=0
    let mid=0
    let h=nums.length-1
    
    while(mid<=h){
        if(nums[mid]==0){
            let t = nums[l]
            nums[l] = nums[mid]
            nums[mid] = t
            l++
            mid++
        }
        else if(nums[mid]==1){
            mid++
        }
        else if(nums[mid]==2){
            let t = nums[h]
            nums[h] = nums[mid]
            nums[mid] = t
            h--            
        }
    }    
    
}