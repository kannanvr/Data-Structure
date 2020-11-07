# Python program to construct tree using
# inorder and level order traversals

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


"""Recursive function to construct binary tree of size n from 
Inorder traversal ino[] and Level Order traversal level[]. 
The function doesn't do any error checking for cases 
where inorder and levelorder do not form a tree """


def buildTree(level, ino):
    # If ino array is not empty
    if ino:

        # Check if that element exist in level order
        for i in range(0, len(level)):

            if level[i] in ino:
                # Create a new node with
                # the matched element
                node = Node(level[i])

                # Get the index of the matched element
                # in level order array
                io_index = ino.index(level[i])
                break

        # If inorder array is empty return node
        if not ino:
            return node

        # Construct left and right subtree
        node.left = buildTree(level, ino[0:io_index])
        node.right = buildTree(level, ino[io_index + 1:len(ino)])
        return node


def printInorder(node):
    if node is None:
        return

    # first recur on left child
    printInorder(node.left)

    # then print the data of node
    print(node.data, end=" ")

    # now recur on right child
    printInorder(node.right)


# Driver code

levelorder = [20, 8, 22, 4, 12, 10, 14]
inorder = [4, 8, 10, 12, 14, 20, 22]

ino_len = len(inorder)
root = buildTree(levelorder, inorder)

# Let us test the build tree by
# printing Inorder traversal
print("Inorder traversal of the constructed tree is")
printInorder(root)

# This code is contributed by 'Vaibhav Kumar'
