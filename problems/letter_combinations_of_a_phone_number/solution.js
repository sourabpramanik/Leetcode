/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    
    if(digits === '') return [];
    let map = {
        2 : "abc", 
        3 : "def", 
        4 : "ghi", 
        5 : "jkl", 
        6 : "mno", 
        7 : "pqrs", 
        8 : "tuv", 
        9 : "wxyz", 
    }
    
    let sub=letterCombinations(digits.slice(1));
    let start=digits[0]
    let arr=[]

    for(let ch of map[start]){
        for(let str of sub) {
            arr.push(ch+str);
        }
    }
    if(arr.length === 0) arr=[...map[start]]
    return arr;
    
};