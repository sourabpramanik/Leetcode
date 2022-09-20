/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let ans = []
    let n = candidates.length

    const rec = (i, ds, t) => {
        if(i==n){
            if(t==0){
                ans.push(ds.slice())
            }
            return
        }
        
        if(candidates[i]<=t){
            ds.push(candidates[i])
            rec(i, ds, t-candidates[i])
            ds.pop()
        }
        rec(i+1, ds, t)
    }
    
    rec(0, [], target)
    
    return ans
};