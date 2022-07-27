/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let arr = []
    let j=0
    for(let i=0; i<n; i++){
        arr[j]=nums[i];
        j++;
        arr[j]=nums[i+n];
        j++
    }
    return arr
};