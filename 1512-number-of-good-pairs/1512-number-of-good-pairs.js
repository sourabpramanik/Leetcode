/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let count=0
    for(let i=0; i<nums.length; i++){
        j=i+1;
        while(j<nums.length){
            if(nums[i]==nums[j]){
                count++
            }
            j++
        }
    }
    return count
};