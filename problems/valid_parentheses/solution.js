/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
    if(s.length%2!==0) return false;
        
    let map = {
        "{" : "}",
        "(" : ")",
        "[" : "]"
    }
    
    let i=0;
    
    let arr = []
    
    while (i<s.length){
        if(map[s[i]]){
            arr.push(map[s[i]])
        } else if(s[i]!==arr.pop()){
            return false;
        }    
        i++
    }       
    
    
    return arr.length===0
};