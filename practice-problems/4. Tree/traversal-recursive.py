def topViewUtil(root, m, hd, height):
    if root == None:
        return
    if hd not in m:
        m[hd] = [root.data, height]
    elif m[hd][1] > height:
        # if we will not put this condition then will not insert the data into map in level order manner . construct
        # tree 1L2, 1R3 2R4 3L5 4L6 4R7, if we not use this cond then o/p: 2 1 7 which is wrong, o/p should be: 2 1 3
        m[hd] = [root.data, height]
    topViewUtil(root.left, m, hd - 1, height + 1)
    topViewUtil(root.right, m, hd + 1, height + 1)


def topView(root):
    if root == None:
        return
    d = dict()
    topViewUtil(root, d, 0, 0)
    a = []
    for i in d.keys():
        a.append(i)
    a.sort()
    for i in a:
        print(d[i][0], end=' ')


def bottomViewUtil(root, mp, hd, h):
    if root == None:
        return
    if hd not in mp:
        mp[hd] = [root.data, h]
    elif mp[hd][1] <= h:
        mp[hd] = [root.data, h]

    bottomViewUtil(root.left, mp, hd - 1, h + 1)
    bottomViewUtil(root.right, mp, hd + 1, h + 1)


def bottomView(root):
    if root == None:
        return
    mp = dict()
    bottomViewUtil(root, mp, 0, 0)
    a = []
    for i in mp:
        a.append(i)
    a.sort()
    for i in a:
        print(mp[i][0], end=' ')


# recursive approach for inorder traversal time: O(n) space: O(h)
def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)


# Recursive approach to write preorder traversal
def preOrder(root):
    if root != None:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)


# Recursive approach to write postorder traversal
def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=' ')


# Function to print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)

# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


""" Compute the height of a tree--the number of nodes
	along the longest path from the root node down to
	the farthest leaf node
"""


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
