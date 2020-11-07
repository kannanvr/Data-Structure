package linkedlist

import (
	"fmt"
)

type Node struct {
	data string
	next *Node
}
//approach1: (use stack) time: O(n), Space: O(n)
/*
1. Traverse the given list from head to tail and push every visited node to stack.
2. Traverse the list again and for every visited node pop an element from stack and compare it.
3. if all nodes matched then return true else false.
eg1: i/p: R->A->D->A->R  o/p: true
 */
func isLinkedlistPalin(head *Node) bool  {
	if head == nil {
		return true
	}
	stack :=make([]string,0)
	node := head
	for node !=nil {
		stack=append(stack,node.data)
		node = node.next
	}
	var data string
	for head !=nil {
		data,stack = stack[len(stack)-1],stack[:len(stack)]
		if data != head.data{
			return false
		}
		head = head.next
	}
	return true
}

//approach 2: Reverse Linked list, time:O(n), space: O(1)
/*
1. get middle of the linked list.(using two pointer, move one pointer by one and other pointer by two.)
2. reverse the second half of the linked list.
3. check if the first and second half are identical.
4. construct the original link list by reversing the second half again.
 */
func isLinkedlistPalin1(head *Node) bool {
	reverse_ptr,mid_node := getMiddleOfList(head)
	reversed_head := reverseList(reverse_ptr)


}
func getMiddleOfList(node *Node) (*Node,*Node) {
	slow_ptr,fast_ptr := node,node
	var midnode *Node
	for fast_ptr != nil && fast_ptr.next != nil {
		fast_ptr=fast_ptr.next.next
		slow_ptr=slow_ptr.next
	}
	fmt.Printf("Middle element is %s",slow_ptr.data)
	//fast ptr would become nil in case of even number of elements and not nil in case of odd number of elements
	//we need to skip the middle node for odd case and store it somewhere so that we can restore the original list.
	if fast_ptr != nil {
		midnode = slow_ptr
		slow_ptr=slow_ptr.next
	}
	return slow_ptr, midnode
}

func reverseList(node *Node) *Node  {
	var tmp,prv *Node
	curr :=node
	for curr != nil {
		tmp = curr.next
		curr.next= prv
		prv=curr
		curr=tmp
	}
	node=prv
	return node
}
/*

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    #A : [ 1 -> 1 -> 6 -> 4 -> 1 ]
    def lPalin(self, A):
        #get middle of the list
        slow,fast=A,A
        mid=None
        while fast.next!=None and fast.next.next != None:
            fast=fast.next.next
            slow=slow.next
        if fast !=None:
            mid=slow
            slow=slow.next
        #print(mid.val,slow.val)
        #reverse 2nd half
        tmp,prv=None,None
        curr = slow
        while curr !=None:
            tmp=curr.next
            curr.next=prv
            prv=curr
            curr=tmp
        rvs_head=prv
        #print(rvs_head.val,rvs_head.next.val)
        while A!=None and rvs_head!=None:
            if A.val != rvs_head.val:
                return 0
            A=A.next
            rvs_head=rvs_head.next
        return 1


*/