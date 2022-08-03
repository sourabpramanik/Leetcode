/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    
   return s.split("").reduce((f, c) => {
      c==="L" ? f.count++ : f.count--;
      f.count===0 && f.ans++
       return f
    }, {count: 0, ans: 0}).ans
};