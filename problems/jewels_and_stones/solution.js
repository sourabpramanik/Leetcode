/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    let map = {};
    
    for(let i=0; i<jewels.length; i++){
        map[jewels[i]] = 0;
    }
    for( const stone of stones){       
        if(map[stone]!==undefined){
            map[stone]++            
        }
    }
    return Object.values(map).reduce((acc, e) => acc + e)
    
};