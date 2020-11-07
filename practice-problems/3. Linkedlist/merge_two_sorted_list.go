package linkedlist
/*
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1
        head= l1 if l1.val<l2.val else l2
        tmp=None
        while l1 and l2:
            if l1.val<l2.val:
                if tmp==None:
                    tmp=l1
                else:
                    tmp.next=l1
                    tmp=tmp.next
                l1=l1.next
            else:
                if tmp==None:
                    tmp=l2
                else:
                    tmp.next=l2
                    tmp=tmp.next
                l2=l2.next
        if l1:
            tmp.next=l1
        if l2:
            tmp.next=l2
        return head





*/
