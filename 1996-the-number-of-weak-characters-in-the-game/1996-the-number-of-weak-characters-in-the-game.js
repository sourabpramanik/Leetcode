/**
 * @param {number[][]} properties
 * @return {number}
 */
var numberOfWeakCharacters = function(properties) {
    properties.sort((a, b) => {
        if(a[0] === b[0]){
            return b[1]-a[1]
        }
        return a[0] - b[0]
    })
    console.log(properties)
    let count = 0
    let min = -Infinity
    for(let i=properties.length-1; i>=0; i--){
        if(properties[i][1]<min){
            count++          
        }
        min = Math.max(min, properties[i][1])
    }
    
    return count
};