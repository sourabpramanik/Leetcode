/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums = nums.sort((a,b) => a-b);
    let len = nums.length;
    let arr = [];
    
    for(let i=0; i<len; i++){
        for(let j=i+1; j<nums.length; j++){
            let k=j+1;
            let l=len-1;
            while(k<l){
                let sum = nums[i] + nums[j] + nums[k] + nums[l];
                if(sum>target){
                    l--
                } else if(sum<target){
                    k++
                } else if(sum==target){
                    arr.push([nums[i], nums[j], nums[k], nums[l]])
                    while(k<l && nums[k]==nums[k+1])k++ 
                    while(k<l && nums[l]==nums[l-1])l--
                    k++
                    l--
                }
            }
            while(nums[j]==nums[j+1])j++;
        }
        while(nums[i]==nums[i+1])i++;       
    }
    return arr
};