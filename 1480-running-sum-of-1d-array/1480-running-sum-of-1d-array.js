/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let num = 0
    let newArr=[]
    for(let i=0; i<nums.length; i++){
        num = nums[i] + num
        newArr.push(num)
    }
    return newArr
};