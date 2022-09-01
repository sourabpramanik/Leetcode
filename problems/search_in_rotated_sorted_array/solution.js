/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    
    if(nums.length==1) return nums[0]==target?0:-1
    let s=0
    let e=nums.length-1       
    
    while(s<=e){
        let mid = Math.floor((s+e)/2)
        if(nums[mid]==target){
            return mid
        }
        if(nums[s]<=nums[mid]){
            if(nums[s]<=target && target<=nums[mid]){
                e=mid-1
            }else{
                s=mid+1
            }
        }else{
            if(nums[mid]<=target && target<=nums[e]){
                s=mid+1
            }else{
                e=mid-1
            }
        }
                
    }
    
    return -1
};