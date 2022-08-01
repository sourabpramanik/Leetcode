/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
    let result = []    
    nums = nums.sort((a,b) => a-b);    
    let i=0;    

    while(i<nums.length-2){
       if(i==0 || nums[i-1]!==nums[i]){
           let j=i+1;
           let k=nums.length-1; 

            while(j<k){
                let first = nums[i], sec = nums[j], last = nums[k];
                let sum = first + sec + last;
                if(sum>0){
                    k--
                } else if(sum<0){
                    j++
                } else if(sum==0){
                    result.push([first, sec, last])
                    while(j<k && nums[j]==nums[j+1]) j++;
                    while(j<k && nums[k]==nums[k-1]) k--;
                    j++;
                    k--
                }
            }
       }
        i++        
    }
    return result
};