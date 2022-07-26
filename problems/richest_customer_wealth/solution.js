/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let wealth = 0;
    let i=0;
    while(i<accounts.length){
        let sum = accounts[i].reduce((acc, e) => acc + e);
        if(sum>wealth){
            wealth=sum;            
        }
        i++
    }
    return wealth
};