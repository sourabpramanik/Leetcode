/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    let s=Array(n+1).join(".")
    let board=Array(n).fill(s)
    let ans=[]
    
    let left=Array(n).fill(0)
    let upD=Array(2*n).fill(0)
    let lowD=Array(2*n).fill(0)
    
    const helper = (col, board) => {
        if(col==n){
            ans.push(board.slice())
            return
        }
        for(let row=0; row<n; row++){
            let sArr;
            if(left[row]==0 && upD[(n-1)+(col-row)]==0 && lowD[row+col]==0){
                left[row] = 1 
                upD[(n-1)+(col-row)] = 1 
                lowD[row+col] = 1                
                sArr = board[row].split("")
                sArr[col]="Q"
                board[row] = sArr.join("")
                
                helper(col+1, board)
                
                left[row] = 0
                upD[(n-1)+(col-row)] = 0
                lowD[row+col] = 0
                sArr = board[row].split("")
                sArr[col]="."
                board[row] = sArr.join("")
            }
        }
    }
    
    helper(0, board)
    return ans
};