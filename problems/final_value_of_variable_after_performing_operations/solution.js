/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let i=0;
    let x=0;
    while(i<=operations.length){
        if(operations[i]==="--X" || operations[i]==="X--"){
            x--
        } else if(operations[i]==="++X" || operations[i]==="X++"){
            x++
        }
        i++
    }
    return x
    
};