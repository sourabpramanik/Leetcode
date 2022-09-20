/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(c, target) {
    let ans = []
    let n = c.length
    c.sort((a,b) => a-b)
      
    function helper(i, t, ds){
        if(t==0){
            ans.push(ds.slice())
            return
        }        
        
        for(let j=i; j<n; j++){
            if(j>i && c[j]==c[j-1]) continue
            if(t<c[j]) break
            
            ds.push(c[j])
            helper(j+1, t-c[j], ds)
            ds.pop()
        }
    }
    helper(0, target, [])
    return ans
};