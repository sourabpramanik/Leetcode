/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if(intervals.length<2){
        return intervals
    }
    intervals.sort((a,b) => a[0]-b[0])
    let ans=[]  
    for(let i=0; i<intervals.length; i++){
        let col=intervals[i]
        
        if(ans.length==0 || ans[ans.length-1][1]<col[0]){
            ans.push(col)
        }
        
        else{     
            
            ans[ans.length-1][1]=Math.max(col[1], ans[ans.length-1][1])
        }
    }
    
    return ans
};