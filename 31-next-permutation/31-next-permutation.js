/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    if(nums.length<2 || nums==null) return;
    let i = nums.length-2
    
    while(i>=0 && nums[i]>=nums[i+1]){
        i--
    }
    
    if(i>=0){
        let j=nums.length-1
        while(nums[j]<=nums[i]){
            j--
        }
        swap(nums, i, j)        
    }
    
    reverse(nums, i+1, nums.length-1)
}

function swap(arr, i, j){
    let temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
}
    
function reverse(arr, i, j){
    while(i<j){
        swap(arr, i, j)
        i++
        j--
    }
}