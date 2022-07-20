/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {};
    let newArr = [];
    for(let i=0; i<nums.length; i++){
        let rem = target-nums[i];        
        if(!map.hasOwnProperty(rem)){
                map[nums[i]]=i;
            } else {
                newArr[0]=i;
                newArr[1]=map[rem];
            }
    }
    return newArr;
};