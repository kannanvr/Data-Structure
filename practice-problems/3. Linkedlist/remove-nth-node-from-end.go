package linkedlist
/*
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        l,curr=0,A
        head=A
        while curr!=None:
            l+=1
            curr=curr.next
        if B>l or l-B+1==1: #remove head node
            return A.next
        if l==1:
            return None
        c=0
        prv=None
        while c<(l-B+1)-1 and A.next != None: #get previous node
            c+=1
            prv=A
            A=A.next
        prv.next=A.next
        return head




*/