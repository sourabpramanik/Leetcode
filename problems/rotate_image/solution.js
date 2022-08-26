/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let rows=matrix.length
    let cols=matrix[0].length
    
    let l = 0
    let r = rows-1
    
    while(l<r){
        let t = matrix[l]
        matrix[l] = matrix[r]
        matrix[r] = t
        l++
        r--
    }
    
    for(let i=0; i<matrix.length; i++){
        for(let j=i+1; j<matrix.length; j++){
            let t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t
        }
    }
};