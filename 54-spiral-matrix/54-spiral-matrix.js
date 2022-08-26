/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let top=0
    let bottom=matrix.length
    let left=0
    let right=matrix[0].length
    let ans=[]
    
    while(top<bottom && left<right){
        for(let i=left; i<right; i++){
            ans.push(matrix[top][i])
        }
        top++
        
        for(let i=top; i<bottom; i++){
            ans.push(matrix[i][right-1])
        }
        right--
        
        if(top<bottom){
            for(let i=right-1; i>=left; i--){
                ans.push(matrix[bottom-1][i])
            }
            bottom--
        }
        if(left<right){
            for(let i=bottom-1; i>=top; i--){
                ans.push(matrix[i][left])
            }
            left++
        }
    }
    
    return ans
};