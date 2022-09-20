/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let ans = []
    let n = candidates.length
    let ds = []
    const rec = (i, t) => {
        if(t==0){
            ans.push(ds.slice())
        }
        if(i==n) return
        if(t<=0) return
        
        if(candidates[i]<=t){
            ds.push(candidates[i])
            rec(i, t-candidates[i])
            ds.pop()
        }
        rec(i+1, t)
    }
    
    rec(0, target)
    
    return ans
};