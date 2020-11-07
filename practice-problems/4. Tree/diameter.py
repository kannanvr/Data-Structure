# function should return the diameter of the tree
def height(root):
    if root == None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def diameter(root):
    # Code here
    if root == None:
        return 0
    x = height(root.left) + 1 + height(root.right)
    y = diameter(root.left)
    z = diameter(root.right)
    return max(x, y, z)
