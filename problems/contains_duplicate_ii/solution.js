/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let i=0;
    let map = [];
    
    while(i<nums.length){
        if(Math.abs(i - map[nums[i]])<=k){
            return true
        }
        map[nums[i]] = [i] ;
        i++;
    }
    return false
};