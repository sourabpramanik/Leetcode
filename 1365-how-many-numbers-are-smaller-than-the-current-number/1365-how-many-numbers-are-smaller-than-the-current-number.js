/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let arr = []
    
    for(let i=0; i<nums.length; i++){
        arr[i]=0
        
        for(let j=0; j<nums.length; j++){
            if(i!==j){
                if(nums[i]>nums[j]){
                    arr[i]++
                }
            }
        }
    };
      
    return arr
};