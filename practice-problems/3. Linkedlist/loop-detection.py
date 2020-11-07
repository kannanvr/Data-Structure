#  Floyd’s loop detection algorithm
def detectLoop(head):
    # code here
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


''' 
https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
find starting point of a loop in a linklist
1. If a loop is found, initialize slow pointer to head, let fast pointer be at its position.
2. Move both slow and fast pointers one node at a time.
3. The point at which they meet is the start of the loop.
check out the proof in above link
'''


def detectLoop_starting(head):
    # code here
    fast = slow = tmp = head
    while fast and fast.next:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next
    if slow != fast:
        return None  # loop doesn't exist
    slow = tmp
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def remove_loop(head):
    # code here
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return None  # loop doesn't exist
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None
    return head
