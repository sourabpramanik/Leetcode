/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    let arr = [];
    for(let num of nums){
        arr.push(num.toString());
    }
    
    arr.sort((a,b)=> (b+a).localeCompare(a+b))
    
    return arr[0]==="0"? "0" : arr.join("")
};