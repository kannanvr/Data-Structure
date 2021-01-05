# a-ans(iterative approach):
def reverse_singly_linkedlist(head):
    prv = None
    current = head
    while current:
        tmp = current.next
        current.next = prv
        prv = current
        current = tmp
    head = prv
    return head


# b-ans(recursive approach):
def reverse_singly_linkedlist_1(head):
    if head is None or head.next is None:
        return head
    # reverse the rest list and put the first element at the end
    node = reverse_singly_linkedlist_1(head.next)
    head.next.next = node
    head.next = None
    return node


# b-ans(using stack): # Time: O(n) and space: O(n)
def reverse_singly_linkedlist_(head):
    stack, current = [], head
    while current.next:  # Push the elements of list to stack
        stack.append(current)
        current = current.next
    head = current  # make last node as head
    while len(stack) > 0:  # Pop from stack and replace current nodes value
        current.next = stack.pop()
        current = current.next
    current.next = None
    return head


# Recursive Python3 program to reverse
# a linked list
import math


# Link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def LinkedList():
    head = None


# Function to reverse the linked list
def reverse(node):
    if node == None or node.next == None:
        print("h",node.data)
        return node
    print("n",node.data)
    node1 = reverse(node.next)
    print(node1.data,node.data)
    node.next.next = node
    node.next = None
    return node1


# Function to print linked list
def printList():
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
    print()


def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref


# Driver Code
if __name__ == '__main__':
    # Start with the empty list
    head = LinkedList()
    head = push(head, 20)
    head = push(head, 4)
    head = push(head, 15)
    head = push(head, 85)

    print("Given linked list")
    printList()

    head = reverse(head)

    print("\nReversed Linked list")
    printList()

# This code is contributed by AbhiThakur
