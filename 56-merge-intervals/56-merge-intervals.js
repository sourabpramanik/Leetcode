/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    let i=0;
    intervals.sort((a,b) => a[0] - b[0])
    while(i<intervals.length-1){
        let block1 = intervals[i];
        let block2 = intervals[i+1];
        
        if(block1[1]>=block2[0]){             
            let start = block1[0]   
            let end = Math.max(block1[1], block2[1])
            intervals.splice(i, 2, [start,end])                              
        } else{
            i++            
        }
    }
    return intervals
};