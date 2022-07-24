/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    let curr=new ListNode(0);
    curr.next=head; head=curr;    
    while(curr.next!==null){
        curr.next.val===val?curr.next=curr.next.next:curr=curr.next;
    }
    return head.next;  
};