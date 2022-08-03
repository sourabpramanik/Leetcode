/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    if(sentences.length==1) return sentences[0].split(" ").length;
    
    let maxLen = sentences[0].split(" ").length
    let i=1;
    
    while(i<sentences.length){
        if(maxLen<sentences[i].split(" ").length){
           maxLen = sentences[i].split(" ").length
        }
        i++
    }
    return maxLen
};