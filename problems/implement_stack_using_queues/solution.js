
var MyStack = function() {
    this.arr = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    this.arr.push(x);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    const last = this.arr[this.arr.length-1];
    this.arr.pop();
    return last;
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    
    return this.arr[this.arr.length-1];
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return this.arr.length===0 ? true : false;
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */