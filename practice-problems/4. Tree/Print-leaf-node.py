# Python3 program to print
# leaf nodes from right to left

# Binary tree node
class newNode:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to print leaf nodes from right to left
def printLeafNodes(root):
	# If node is null, return
	if root == None:
		return
	# If node is leaf node,  print its data
	if (root.left == None and root.right == None):
		print(root.data, end = " ")
		return
	# If right child exists, check for leaf recursively
	if root.right:
		printLeafNodes(root.right)
	# If left child exists, check for leaf recursively
	if root.left:
		printLeafNodes(root.left)

# Function to print leaf nodes from right to left
def printLeafNodes(root):
	# If node is null, return
	if root == None:
		return
	# If node is leaf node,  print its data
	if (root.left == None and root.right == None):
		print(root.data, end = " ")
		return
	# If left child exists, check for leaf recursively
	if root.left:
		printLeafNodes(root.left)
	# If right child exists, check for leaf recursively
	if root.right:
		printLeafNodes(root.right)

# Driver code
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.left.left.left = newNode(8)
root.right.right.left = newNode(9)
root.left.left.left.right = newNode(10)

printLeafNodes(root)
