/**
 * @param {number[]} nums
 * @return {number}
 */
class Node{
    constructor(){
        this.links = {}
    }
}

class Trie{
    constructor(){
        this.root = new Node()
    }
    
    insert(num){
        let root = this.root
        for(let i=31; i>=0; i--){
            let bit = (num>>i) & 1
            if(root.links[bit]===undefined){
                root.links[bit] = new Node()
            }
            root = root.links[bit]
        }
    }
    
    getMax(num){
        let root = this.root
        let maxim = 0
        for(let i=31; i>=0; i--){
            let bit = (num>>i) & 1
            if(root.links[(1-bit)]!==undefined){
                maxim = maxim | (1<<i)
                root = root.links[(1-bit)]
            }
            else{
                root = root.links[bit]
            }
        }
        return maxim
    }
}
var findMaximumXOR = function(nums) {
    let trie = new Trie()
    
    for(let i=0; i<nums.length; i++){
        trie.insert(nums[i])
    }
    
    let max = 0
    for(let i=0; i<nums.length; i++){
        max = Math.max(max, trie.getMax(nums[i]))
    }
    
    return max
};