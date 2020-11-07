//package sorting
package main

import "fmt"

//given an array and an element x of array as pivot put x as its correct position in sorted array.
//ie. all smaller elements before x and all larger elements after x
func Partition(arr []int, low, high int) int {
	i := low - 1       //index of smaller element
	pivot := arr[high] //pivot
	for j := low; j < high; j++ {
		if arr[j] < pivot { //if arr[j]%2==0 then all even elements will come to left and odd shift to right
			i++ //increment index of smaller element
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1
}

//we can take the pivot element as first,last mid or any random element.
//here we r assuming right most element is always pivot element.
func quickSort(arr []int, low, high int) { //low--->starting index , high ---> ending index
	if low < high {
		pi := Partition(arr, low, high) //pi is partitioning index
		fmt.Println(pi, arr[pi], arr)
		//sot left half and right half in recursive manner
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
	}
}

func main() {
	arr := []int{10, 7, 8, 9, 1, 5, 12, 65, 68}
	quickSort(arr, 0, len(arr)-1)
	fmt.Println("Sortred array: ", arr)
}
