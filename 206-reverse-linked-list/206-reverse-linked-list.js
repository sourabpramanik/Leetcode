/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
   
   
   
    function help(curr, prev){
        if(curr==null) return prev
        let next = curr.next
        curr.next = prev
        prev = curr
        return help(next, prev)
    }
    
    
    
    return help(head, null)
};