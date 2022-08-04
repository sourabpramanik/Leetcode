/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = new Map();
    let ans = []
    for(let str of strs){
        let sortedStr =  [...str].sort().join("")
        if(!map.has(sortedStr)){
            map.set(sortedStr, [])
        } 
        map.get(sortedStr).push(str)
    }
    for(let [,values] of map){
        ans.push(values)
    }
    return ans
};