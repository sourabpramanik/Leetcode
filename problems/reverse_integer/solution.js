/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
   
    let num = Math.abs(x);
    
    let rev = 0;
    
    while(num){
        rev = rev*10 + (num%10);
        num = Math.floor(num/10)
    }
    
    if( rev > 0x7FFFFFFF )  return 0;
    
    return x<0 ? rev * -1 : rev
};