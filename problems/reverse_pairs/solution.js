/**
 * @param {number[]} nums
 * @return {number}
 */
var reversePairs = function(nums) {
    
    let count=0
    helper(nums)
    return count
    
    function helper(nums){
        if(nums.length<=1) return nums
        
        let left = helper(nums.slice(0, Math.floor(nums.length/2)))
        let right = helper(nums.slice(Math.floor(nums.length/2)))
        return merge(left, right)
    }
    
    function merge(left, right){
        let sorted=[]
        let i=0, j=0
        
        while(i<left.length && j<right.length){
            if(left[i]>2*right[j]){
                count+=(left.length -i)
                j++
            }else{
                i++
            }    
        }
        i=0
        j=0
        
        while(i<left.length && j<right.length){
            if(left[i]<right[j]){
                sorted.push(left[i])
                i++
            }else{
                sorted.push(right[j])
                j++
            }    
        }
        while(i<left.length){
            sorted.push(left[i])
            i++    
        }
        while(j<right.length){
            sorted.push(right[j])
            j++    
        }
        
        return sorted
    }
};