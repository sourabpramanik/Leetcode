/**
 * @param {string} s
 * @param {number[]} distance
 * @return {boolean}
 */
var checkDistances = function(s, distance) {
    let map={}
    let alph="abcdefghijklmnopqrstuvwxyz".split("")
    
    for(let i=0; i<s.length; i++){
        if(map[s[i]]===undefined){
            map[s[i]]=i
        }else{
            if(distance[alph.indexOf(s[i])]!=Math.abs(i-map[s[i]]-1)) return false           
        }
    }
    return true
};