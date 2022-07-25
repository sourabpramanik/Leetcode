/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let len = nums.length;
  let nums1 = [], ans = [];

  for(let i=0; i<len; i++){
      nums1[i] = nums[i];
  }

  ans = nums.concat(nums1);
  return ans;
};