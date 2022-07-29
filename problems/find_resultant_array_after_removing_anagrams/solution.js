/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function(words) {
    let prev = "";
    let arr = []
    for(let word of words){
        let sorted = word.split("").sort().join("");
        if(sorted!==prev) {
            arr.push(word)
        }
        prev = sorted;
    }
    return arr
};