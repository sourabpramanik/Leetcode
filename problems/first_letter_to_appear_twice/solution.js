/**
 * @param {string} s
 * @return {character}
 */
var repeatedCharacter = function(s) {
    let map = {}
    
    for(let ch of s){
        if(!map[ch]){
            map[ch] = 1
        } else{
            return ch
        }
    }
};