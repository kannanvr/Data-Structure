package main

import "fmt"

//www.geeksforgeeks.org/heap-sort/amp/

//to heapify subtree rooted at index i and size of hep is n.
func heapify(arr []int, n, i int) {
	largest := i //initialize largest as root
	l := 2*i + 1 //left child position
	r := 2*i + 2 //right child position
	//if left child exist and greater than root then update largest index
	if l < len(arr) && arr[l] > arr[i] {
		largest = l
	}
	//if right child exist and greater than root then update largest index
	if r < len(arr) && arr[r] > arr[largest] {
		largest = r
	}
	//if largest is not root
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest) //recursively heapify the affected subtree
	}
}

func heapSort(arr []int, n int) {
	fmt.Printf("array before building heap %v\n", arr)
	//build heap ( rearrange elements )
	for i := int(n / 2); i >= 0; i-- { // 0-n/2-1 ---> parent nodes and n/2-n--->leaf nodes
		heapify(arr, n, i)
	}
	fmt.Printf("array after building heap %v\n", arr)
	//one by one extract an element from heap
	for i := n - 1; i >= 0; i-- {
		//swap(arr[0],arr[i])
		arr[0], arr[i] = arr[i], arr[0]
		//call the max hepify on the reduced heap
		heapify(arr, i, 0)
	}

}
func main() {
	arr := []int{10, 7, 8, 9, 1, 5, 12, 65, 68}
	heapSort(arr, len(arr))
	fmt.Println("Sortred array: ", arr)
}

