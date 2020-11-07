class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        # Allocate new node
        new_node = Node(new_value)
        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        # Append the new node at the end of the linked list
        # while curr_node.next is not None:
        #    curr_node = curr_node.next
        # curr_node.next = new_node
        # Append the new node at the front of the linked list
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end='->')
            curr_node = curr_node.next
        print()


def pairWiseSwap(head):
    # code here
    if head.next is None:
        return head
    p1 = head
    p2 = p1.next
    while p2:
        p1.data, p2.data = p2.data, p1.data
        p1 = p2.next
        if p1==None:
            break
        p2 = p1.next

    return head


if __name__ == '__main__':
    li = LinkedList()
    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)
    print("Link list before swapping")
    li.printList()
    pairWiseSwap(li.head)
    print("Link list after swapping")
    li.printList()
