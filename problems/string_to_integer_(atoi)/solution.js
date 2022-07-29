/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    s = parseInt(s)
    if((isNaN(s)))return 0

    if(s> 0x7FFFFFFF) return 2147483647
    if(s < -0x7FFFFFFF) return -2147483648
    return s
};