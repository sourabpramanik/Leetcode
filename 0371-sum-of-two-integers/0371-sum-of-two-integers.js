/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    
    let c = 0
    while(b!==0){
        c = a&b
        a = a^b
        b = c<<1        
    }
    return a
};