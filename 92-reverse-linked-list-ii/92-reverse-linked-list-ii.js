/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    let dummy = new ListNode(0)
    dummy.next = head
    
    let pre = dummy
    for(let i=0; i<left-1; i++){
        pre = pre.next
    }
    
    let s = pre.next
    let n = s.next
    
    for(let i=0; i<right-left; i++){
        s.next = n.next
        n.next = pre.next
        pre.next = n
        n = s.next
    }
    
    return dummy.next
};