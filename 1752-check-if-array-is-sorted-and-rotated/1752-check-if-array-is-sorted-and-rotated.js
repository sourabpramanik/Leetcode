/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(a) {
   
    let k=0
    for(let i=0; i<a.length; i++){    
        if(a[i]>a[(i+1)%a.length]){
            k++
        }
        if(k>1){
            return false
        }
    }
    
    return true
};