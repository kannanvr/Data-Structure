package linkedlist
/*
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        a,b="",""
        while A!=None:
            a+=str(A.val)
            A=A.next
        while B!=None:
            b+=str(B.val)
            B=B.next
        result=str(int(a[::-1])+int(b[::-1]))[::-1]
        #print(a,b,result)
        c=0
        head,curr=None,None
        while c<len(result):
            if head==None:
                curr=head=ListNode(result[c])
            else:
                curr.next=ListNode(result[c])
                curr=curr.next
            c+=1
        return head





*/
