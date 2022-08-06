/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
var decodeMessage = function(key, message) {
    let map = {};
    let idx= 0;
    for(let char of key){
        if(char!=" " && !map[char]){
            map[char] = String.fromCharCode(idx + 97);
            idx++
        }
    }
    
    map[" "] = " ";
    return message.split("").map(c => map[c]).join("")
    
    
};