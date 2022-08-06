/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let count=0
    for(let i=0; i<words.length; i++){
        let d = [...words[i]].filter(e => !allowed.includes(e) && e );
        if(d.length===0){
            count++
        }
    }
    return count
};