/**
 * @param {number} x
 * @return {boolean}
 */

var isPalindrome = function(x) {
    var numArr = x.toString().split("").reverse()
    if(numArr.join("") == x){
        return true
    }
    else return false 
};

