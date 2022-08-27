/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    if(numRows==1){
        return [[1]]
    }
    
    let ans = []
    if(numRows>=1){
        ans.push([1])
        numRows--;
    }
    
    let i=1
    while(i<=numRows){
        let aux=[]
        let row=ans[ans.length-1]
        let first=row[0]
        let last=row[row.length-1]
        aux.push(first)
        if(i>1){
            for(let j=1; j<row.length; j++){
                let sum = row[j]+first
                aux.push(sum)
                first=row[j]
            }
        }
        aux.push(last)    
        ans.push(aux)
        i++
    }
    
    return ans
    
    
    
};