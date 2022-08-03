/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {    
    let map = {};
    for(let i=0; i<indices.length; i++){
        map[indices[i]] = s[i];
    }
    return Object.values(map).join("")
};