def modifyBSTUtil(root, Sum):
    # Base Case
    if root == None:
        return

    # Recur for right subtree
    modifyBSTUtil(root.right, Sum)

    # Now Sum[0] has sum of nodes in right
    # subtree, add root.data to sum and
    # update root.data
    Sum[0] = Sum[0] + root.data
    root.data = Sum[0]

    # Recur for left subtree
    modifyBSTUtil(root.left, Sum)


# A wrapper over modifyBSTUtil()
def modifyBST(root):
    Sum = [0]
    modifyBSTUtil(root, Sum)