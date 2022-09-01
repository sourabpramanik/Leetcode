/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    if(nums.length==1) return nums[0]
    let s=0
    let e=nums.length-1
    let res=Infinity
    while(s<=e){
        if(nums[s]<=nums[e]){
            res = Math.min(nums[s], res)
            break
        }
        
        let mid=Math.floor((s+e)/2)
        if(nums[s]<=nums[mid]){
            res = Math.min(nums[s], res)
            s=mid+1
        }else{
            res = Math.min(nums[mid],res)
            e=mid            
        }
    }
    return res
};