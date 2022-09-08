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
var deleteDuplicates = function(head) {
    if(!head)return head

    function rec(prev, curr){
        if(!curr) return head
        if(prev.val===curr.val){
            prev.next = curr.next
            curr = curr.next
        } else {
            prev = prev.next
        }  
        return rec(prev, curr)
    }
    
    
    return rec(head, head.next)
};