/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(nums.length==0) return 0
    let longStreak = 1
    let hashSet = new Set(nums)
    
    for(let num of nums){
        if(!hashSet.has(num-1)){
            let curNum = num
            let curStreak = 1
            while(hashSet.has(curNum+1)){
                curNum+=1
                curStreak+=1
            }
            longStreak = Math.max(longStreak, curStreak)
        }        
    }
    
    return longStreak
};