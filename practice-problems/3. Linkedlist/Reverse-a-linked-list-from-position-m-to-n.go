package linkedlist
/*
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        org_head=A
        c,head,tail,pre=0,None,None,None
        while A!=None:
            c+=1
            if c==B:
                head_prv=pre
                head=A
            if c==C:
                tail=A
                tail_next=A.next
            if head and tail:
                break
            pre=A
            A=A.next
        #print(head.val,tail.val)
        curr,tmp,prv=head,None,None
        while curr !=None:
            tmp=curr.next
            curr.next=prv
            prv=curr
            if curr==tail:
                break
            curr=tmp
        tail=head
        head=prv
        #print(head.val,tail.val)
        tail.next=tail_next
        if head_prv==None:
            return head
        if head_prv !=None:
            head_prv.next=head
        return org_head

 */
