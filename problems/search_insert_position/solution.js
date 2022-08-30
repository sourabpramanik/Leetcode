/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let s=0
    let e=nums.length-1
    let ans=0
    
    while(s<=e){
        let mid = s + Math.floor((e-s)/2)
        
        if(nums[mid]>target){
            e=mid-1
        }else if(nums[mid]<target){
            ans=mid+1
            s=mid+1
        }else if(nums[mid]==target){
            return mid
        }
    }
    return ans
};