/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = {};
    let ans = []
    for(let str of strs){
        let sortedStr =  [...str].sort().join("")
        if(!map[sortedStr]){
            map[sortedStr] = []
        } 
        map[sortedStr].push(str)
    }
    return Object.values(map)
};