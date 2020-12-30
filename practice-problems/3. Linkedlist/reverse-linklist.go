package linkedlist

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

//iterative approach to reverse a linklist
func reverseList(head *ListNode) *ListNode {
	var tmp, pre *ListNode
	current := head

	for current != nil {
		tmp=current.Next
		current.Next=pre
		pre=current
		current=tmp
	}
	return pre
}
