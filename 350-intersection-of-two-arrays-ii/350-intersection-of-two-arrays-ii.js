/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    let result = []
    for(let i = 0;i<nums1.length;i++){
        if(nums2.includes(nums1[i])){
            result.push(nums1[i])
            let index = nums2.indexOf(nums1[i])
            nums2.splice(index,1)
        }
    }
    return result;
    
};