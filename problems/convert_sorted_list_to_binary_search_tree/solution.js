/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    if(head==null){
        return null
    }
    
    return helper(head, null)
};

var helper = function(head, tail){
    if(head==tail){
        return null
    }
    
    let fast = head
    let slow = head
    
    while(fast!==tail && fast.next!==tail){
        fast = fast.next.next
        slow = slow.next
    }
    
    let root = new TreeNode(slow.val)
    root.left = helper(head, slow)
    root.right = helper(slow.next, tail)
    
    return root
}