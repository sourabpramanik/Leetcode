/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    if(arr.length===1) return [-1]
    
    let j=arr.length-2;
    let max=arr[arr.length-1];
    while(j>=0){
        let curr = arr[j];
        arr[j] = max        
        if(curr > max){
            max=curr                     
        } 
        --j
    }
    arr[arr.length-1] = -1;
    return arr
};