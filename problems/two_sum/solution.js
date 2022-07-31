/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {};
    let arr = [];
    
    for(let i=0; i<nums.length; i++){
        let rem = target - nums[i];
        if(!map[rem]){
            map[nums[i]] = i+1;
        } else{
            arr.push(i, map[rem]-1)
        }
    }
    return arr
};