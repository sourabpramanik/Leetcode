/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    if(nums.length===1){
        return nums
    }
    
    let mid = Math.floor(nums.length/2)
        
    let L = nums.slice(0,mid)
    let R = nums.slice(mid)
    sortColors(L)
    sortColors(R)
    
    let i=0, j=0, k=0
    
    while(i<L.length && j<R.length){
        if(L[i]<R[j]){
            nums[k] = L[i]
            i++
        }else{
            nums[k] = R[j]
            j++
        }
        k++
    }
    
    while(i<L.length){
        nums[k] = L[i]
        i++
        k++
    }
    
    while(j<R.length){
        nums[k] = R[j]
        j++
        k++
    }
    
    return nums
    
};