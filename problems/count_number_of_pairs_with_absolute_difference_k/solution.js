/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countKDifference = function(nums, k) {
    let count=0;
    let map=new Map();
    
    for(let i=0; i<nums.length; i++){
        let num = nums[i];
        map.set(num, (map.get(num) ?? 0)+1)
        count += (map.get(num-k) ?? 0) + (map.get(num+k) ?? 0)
    }

    return count
};