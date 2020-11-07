package main

import (
	"fmt"
)

type Tree struct {
	root *Node
}

type Node struct {
	key   byte
	left  *Node
	right *Node
}

func (t *Tree) insert(data byte) {
	if t.root == nil {
		t.root = &Node{key: data}
	} else {
		t.root.insert(data)
	}
}

func (n *Node) insert(data byte) {
	if data <= n.key {
		if n.left == nil {
			n.left = &Node{key: data}
		} else {
			n.left.insert(data)
		}
	} else {
		if n.right == nil {
			n.right = &Node{key: data}
		} else {
			n.right.insert(data)
		}
	}
}

func printPreOrder(n *Node) {
	if n == nil {
		return
	} else {
		fmt.Printf("%c ", n.key)
		printPreOrder(n.left)
		printPreOrder(n.right)
	}
}

func printPostOrder(n *Node) {
	if n == nil {
		return
	} else {
		printPostOrder(n.left)
		printPostOrder(n.right)
		fmt.Printf("%c ", n.key)
	}
}

func printInOrder(n *Node) {
	if n == nil {
		return
	} else {
		printInOrder(n.left)
		fmt.Printf("%c ", n.key)
		printInOrder(n.right)
	}
}
func inorderTraversal(r *treeNode) []int {
	if r == nil {
		return []int{}
	}

	st := make([]*treeNode, 0)
	node := r
	for node != nil {
		st = append(st, node)
		node = node.left
	}

	result := make([]int, 0)
	for len(st) > 0 {
		node = st[len(st)-1]
		st = st[:len(st) - 1]

		result = append(result, node.value)
		if node.right != nil {

			node = node.right
			for node != nil {
				st = append(st, node)
				node = node.left
			}
		}
	}

	return result
}

func main() {
	var t Tree
	ar := []byte{'F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'}
	for _, v := range ar {
		t.insert(v)
	}
	fmt.Printf("Pre Order: ")
	printPreOrder(t.root)
	fmt.Printf("\nPost Order: ")
	printPostOrder(t.root)
	fmt.Printf("\nIn Order: ")
	printInOrder(t.root)
}
// Pre Order: F B A D C E G I H
// Post Order: A C E D B H I G F
// In Order: A B C D E F G H I