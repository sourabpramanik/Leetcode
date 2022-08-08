/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    let rLen = matrix.length;
    let cLen = matrix[0].length;
    
    let rows = new Set();
    let cols = new Set();
    
    for(let i=0; i<rLen; i++){
        for(let j=0; j<cLen; j++){
            if(matrix[i][j]==0){
                rows.add(i);
                cols.add(j);
            }
        }
    }
    
    for(let i=0; i<rLen; i++){
        for(let j=0; j<cLen; j++){
            if(rows.has(i) || cols.has(j)){
                matrix[i][j]=0
            }
        }
    }
};