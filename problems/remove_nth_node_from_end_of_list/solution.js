/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let ref1 = head;
    let ref2 = head;    
    while(n--){
        ref1 = ref1.next;
    }
    
    if(!ref1) return head.next
    while(ref1.next){
        ref1 = ref1.next;
        ref2 = ref2.next;
    }
    
    ref2.next = ref2.next.next;
    return head
};