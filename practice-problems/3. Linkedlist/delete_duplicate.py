
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
