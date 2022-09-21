/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    let hash = {}
    let ans = []
    nums.sort((a, b) => a-b)
    function rec(i, ds){
        ans.push(ds.slice())   
        
        for(let j=i; j<nums.length; j++){
            if(j>i && nums[j]===nums[j-1]) continue            
            ds.push(nums[j])
            rec(j+1, ds)
            ds.pop()
        }
    }
    
    rec(0, [])
    
    return ans
    
    
};