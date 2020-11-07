class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative function for inorder tree traversal  time: O(n), O(h) height of tree, use MorrisTraversal for O(1) space
# 1) Create an empty stack S.
# 2) Initialize current node as root
# 3) Push the current node to S and set current = current->left until current is NULL
# 4) If current is NULL and stack is not empty then
#     a) Pop the top item from stack.
#     b) Print the popped item, set current = popped_item->right
#     c) Go to step 3.
# 5) If current is NULL and stack is empty then we are done.
def inOrder(root):
    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack
    while True:
        # Reach the left most Node of the current Node
        if current is not None:
            # Place pointer to a tree node on the stack before traversing the node's left subtree
            stack.append(current)
            current = current.left
        # BackTrack from the empty subtree and visit the Node at the top of the stack; however, if the stack is empty you are done
        elif (stack):
            current = stack.pop()
            print(current.data, end=" ")
            # We have visited the node and its left subtree. Now, it's right subtree's turn
            current = current.right
        else:
            break
    print()


# Iterative function for preOrder tree traversal  time: O(n), O(h) height of tree, use MorrisTraversal for O(1) space
# 1) Create an empty stack nodeStack and push root node to stack.
# 2) Do following while nodeStack is not empty.
# ….a) Pop an item from stack and print it.
# ….b) Push right child of popped item to stack
# ….c) Push left child of popped item to stack
def preOrder(root):
    nodeStack = [root]  # initialize stack
    while (len(nodeStack) > 0):
        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.data)
        # Push right and left children of the popped node to stack
        if node.right:
            nodeStack.append(node.right)
        if node.left:
            nodeStack.append(node.left)
    print()


# iterative approach https://www.geeksforgeeks.org/iterative-postorder-traversal/
# 1. Push root to first stack.
# 2. Loop while first stack is not empty
#   2.1 Pop a node from first stack and push it to second stack
#   2.2 Push left and right children of the popped node to first stack
# 3. Print contents of second stack
def postOrderIterative(root):
    if root is None:
        return
    # Create two stacks
    s1 = []
    s2 = []
    # Push root to first stack
    s1.append(root)
    # Run while first stack is not empty
    while s1:
        # Pop an item from s1 and append it to s2
        node = s1.pop()
        s2.append(node)
        # Push left and right children of removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
        # Print all elements of second stack
    while s2:
        node = s2.pop()
        print(node.data)


# Iterative Method to print the height of binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return
    # Create an empty queue for level order traversal
    queue = []
    # Enqueue Root and initialize height
    queue.append(root)
    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print(queue[0].data, end=' ')
        node = queue.pop(0)
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# print levelOrder traversal line by line
def printLevelOrder(root):
    # Base case
    if root is None:
        return
    # Create an empty queue for level order traversal
    q = []
    # Enqueue root and initialize height
    q.append(root)
    while q:
        # nodeCount (queue size) indicates number
        # of nodes at current lelvel.
        count = len(q)
        # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
        while count > 0:
            temp = q.pop(0)
            print(temp.val, end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            count -= 1
        print(' ')



# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Level Order Traversal of binary tree is -")
printLevelOrder(root)
print("\nrecursive inorder: ")
inOrder(root)
print("\nrecursive preorder: ")
preOrder(root)
print("\nrecursive postorder: ")
postOrder(root)
print("\nheight of tree is: ", heightofTree(root))
print("nodes at level 3: ")
printAtGivenLevel(root, 3)
printKDistant(root, 2)
