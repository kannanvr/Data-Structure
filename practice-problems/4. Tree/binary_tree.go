package Tree

//Q. Construct a binary tree from given array of integers! or a complete binary tree from given array in level order fashion.
/*
ar=['A','B','C','D','E','F']
1. consider ar[0] as root node.
2. left child of that node is at index (2*i+1), here parent node is at index i
3. right child is at index (2*i+2)
*/
type node struct {
	data  string
	left  *node
	right *node
}

func newNode(data string) *node {
	return &node{
		data:  data,
		left:  nil,
		right: nil,
	}
}
func makeBinaryTree(root node, data string)  {
	if root == nil {

	}
}

func main() {
	ar := []string{"A", "B", "C", "D", "E", "F"}
	root := node{}
	inOrder(root)
}
