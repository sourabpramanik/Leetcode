/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    if(sentences.length==1) return sentences[0].split(" ").length;
    
    let maxLen = sentences[0].split(" ").length
    
    for(let sentence of sentences){
        maxLen = Math.max(maxLen, sentence.split(" ").length)
    }
    return maxLen
};