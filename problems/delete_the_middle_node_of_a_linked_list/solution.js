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
var deleteMiddle = function(head) {
    let ref = head;
    let len=0;
    while(ref){
        len++;
        ref=ref.next;
    }
    if(len == 1) return ref;
    let pos = Math.floor(len/2);
    ref=head
    let count=1;
    while(ref){
        if(count===pos){
            ref.next = ref.next.next
        }
        count++;        
        
        ref = ref.next
    }
    return head;
};