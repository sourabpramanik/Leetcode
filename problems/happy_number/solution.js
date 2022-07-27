/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {   
    const set = new Set();
    while(n!=1){
        n = [... "" + n].map(num => num*num).reduce((acc, e) => acc+e);
        if(set.has(n)){
            return false;
        } else{
            set.add(n)
        }
        
    }
    return true;
};