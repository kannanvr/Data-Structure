package linkedlist

//Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    current := head
    tmp     := current
    for current != nil {
        if current.Val != tmp.Val {
            tmp=tmp.Next
            tmp.Val=current.Val
        }
        current=current.Next
    }
    tmp.Next=nil
    return head
}

/*
def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    prv, curr = None, head
    while curr:
        if prv == None:
            prv = curr
            curr = curr.next
        elif prv.val == curr.val:
            tmp = curr
            prv.next = curr.next
            curr = curr.next
            tmp.next = None
        else:
            prv = prv.next
            curr = curr.next
    return head
*/