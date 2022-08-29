/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    
    function helper(arr, left, right, val){
        if(left>right) return -1
        
        let mid=left + Math.floor((right-left)/2)
        
        if(arr[mid]==val) return mid
        else if(val>arr[mid]) 
            return helper(arr, mid+1, right, val)
        else 
            return helper(arr, left, mid-1, val)
    }
    
    return helper(nums, 0, nums.length-1, target)
};