/**
 * @param {number} n
 */
var OrderedStream = function(n) {
    this.array = [];
    this.current = 0;
};

/** 
 * @param {number} idKey 
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function(idKey, value) {
    let arr = [];
    
    if(idKey-1 == this.current){
        this.array[idKey-1] = value
        while(this.array[this.current]){
            arr.push(this.array[this.current])
            this.current++
        }
    }
    else{
        this.array[idKey-1] = value
    }
    return arr
};

/** 
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */