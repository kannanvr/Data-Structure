# the worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree.
'''
Searching: worst case complexity(skewed binary tree) of O(n). In general, time complexity is O(h)==O(logn), where h is height of BST for complete bst, height is logn.
Insertion: worst case complexity(skewed binary tree) of O(n). In general, time complexity is O(h)==O(logn),
Deletion: worst case complexity(skewed binary tree) of O(n). In general, time complexity is O(h)==O(logn).
'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to search a given key in BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)
    # Key is smaller than root's key
    return search(root.left, key)


# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


'''
https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
When we delete a node, three possibilities arise.
1) Node to be deleted is leaf: Simply remove from the tree.
2) Node to be deleted has only one child: Copy the child to the node and delete the child
3) Node to be deleted has two children: Find inorder successor of the node.
Copy contents of the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.
inorder successor can be obtained by finding the minimum value in right child of the node.

'''


def deleteNode(root, key):
    if root is None:
        return root
    # If the key to be deleted is smaller than the root's  key then it lies in  left subtree , searching key to be
    # deleted in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
    # If the kye to be delete is greater than the root's key then it lies in right subtree, searching key to be
    # deleted in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    # If key is same as root's key, then this is the node to be deleted, key found
    else:
        # Node with only one child or no child case1 and case2
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children: Get the inorder successor (smallest in the right subtree) or (largest in left subtree)
        temp = minValueNode(root.right)
        # Copy the inorder successor's content to this node
        root.key = temp.key
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
    return root


# Given a non-empty binary search tree, return the node with minimum key value found in that tree. Note that the
# entire tree does not need to be searched
def minValueNode(node):
    current = node
    # loop down to find the leftmost leaf
    while (current.left is not None):  # will get the minimum value in left side
        current = current.left

    return current


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
#	 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80
r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))
# Print inoder traversal of the BST
inorder(r)
# This code is contributed by Bhavya Jain
