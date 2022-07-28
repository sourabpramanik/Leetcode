/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
    
    let res = "";
    let i=0;
    
    while(num>0){
        if(num>=integers[i]){
            res += roman[i];
            num -= integers[i];
        } else{
            i++
        }
    }
    return res
};