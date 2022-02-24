/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var arrNums = [2,7,11,15]
var target = 9
var twoSum = function(nums, target) {
    const newArr = [];
    for(let i = 0; i < nums.length; i++){
        for(let j = i +1; j < nums.length; j++){
            if(nums[i] + nums[j] == target){
                newArr.push(i)
                newArr.push(j)
                return newArr;                
            }        
        }
    }
};

twoSum(arrNums,target)