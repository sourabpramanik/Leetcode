/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let str = strs[0];
    
    if(strs.length===1) return strs[0]
    
    let i=1;
    while(i<strs.length){
        let curr = strs[i]
        for(let j=0; j<str.length; j++){
            if(curr[j] !== str[j]){
                str = str.slice(0,j)
            }
        }
        i++
    }
    return str
        
};