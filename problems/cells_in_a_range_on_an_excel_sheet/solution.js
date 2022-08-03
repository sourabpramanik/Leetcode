/**
 * @param {string} s
 * @return {string[]}
 */
var cellsInRange = function(s) {
    let arr = [];
    let colStart = s.split(":")[0].charCodeAt(0);
    let colEnd = s.split(":")[1].charCodeAt(0)
    let numRow = s.split(":")[1][1]
    for(let i=colStart; i<=colEnd; i++){
        
        let letter = String.fromCharCode(i);        
        for(let j=s.split(":")[0][1]; j<=numRow; j++){
            arr.push(letter + j)
        }
    }
    
    return arr
};