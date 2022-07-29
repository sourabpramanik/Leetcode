/**
 * @param {string[]} words
 * @param {string} pattern
 * @return {string[]}
 */
var findAndReplacePattern = function(words, pattern) {
    let reg1 = pattern.split("").map((e) => pattern.indexOf(e) ).join("")
    return words.filter(e => e.split("").map((i) => e.indexOf(i) ).join("") == reg1)
    
};