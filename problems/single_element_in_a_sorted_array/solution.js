/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    let s=0
    let e=nums.length-1
    while(s<=e){
        let mid = Math.floor((s+e)/2)
        if((mid%2==1 && nums[mid-1]==nums[mid]) || (mid%2==0 && nums[mid+1]==nums[mid])){
            s=mid+1
        }else{
            e=mid-1
        }
    }
    
    return nums[s]
};