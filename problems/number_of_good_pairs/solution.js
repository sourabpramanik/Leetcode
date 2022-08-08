/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let map = {}
    let count=0
    for(let num of nums){
        if(map[num]!==undefined){
            count+=map[num]
        } 
        map[num] = map[num]?map[num]+1:1
    }
    return count
};