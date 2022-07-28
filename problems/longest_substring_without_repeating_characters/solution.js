/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
   let longest=0;
    
    for(let i=0; i<s.length; i++){
        let str=s[i];
        let j=i+1;
        while(j<s.length && str.indexOf(s[j])===-1){
            str += s[j]
            j++
        }
        
        if(str.length>longest){
            longest = str.length;
        }
    }
    return longest;
    
};