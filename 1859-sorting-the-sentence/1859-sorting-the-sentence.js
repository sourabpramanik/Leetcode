/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let arr = s.split(" ");
    let str = [];
    for(let i=0; i<arr.length; i++){
        let idx = arr[i].split("").pop()
        str[idx-1] = arr[i].split("").filter(e=> isNaN(e)).join("")
    }
   
    return str.join(" ")
};