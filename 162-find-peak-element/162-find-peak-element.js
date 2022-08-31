/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    
    if(nums.length==1) return 0
    let s=0
    let e=nums.length-1
    
    while(s<=e){
        let mid=Math.floor((s+e)/2)
        
        if(mid==0){
            return nums[0] >= nums[1] ? 0 : 1
        }
        if(mid==nums.length-1){
            return nums[nums.length-1] >= nums[nums.length-2] ? nums.length-1 : nums.length-2
        }
        if(nums[mid]>=nums[mid-1] && nums[mid]>=nums[mid+1]){
            return mid
        }
        if(nums[mid]<nums[mid-1]){
            e=mid-1
        } else{
            s=mid+1
        }        
    }
    
    return s
    
};