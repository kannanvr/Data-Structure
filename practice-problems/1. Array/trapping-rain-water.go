package Array

// Approach1: The idea is to traverse every array element and find the highest bars on left and right sides.
//Take the smaller of two heights. The difference between the smaller height and
//height of the current element is the amount of water that can be stored in this array element.
// C++ implementation of the approach

// Function to return the maximum
// water that can be stored
func maxWater(arr []int, n int) int{

	// To store the maximum water
	// that can be stored
	var res int = 0
	for i:=1;i<n;i++{
		// Find the maximum element on its left
		var leftMax int = arr[i]
		for j:=0;j<i;j++{
			if arr[j]>leftMax{
				leftMax=arr[j]
			}
		}
		// Find the maximum element on its right
		var rightMax int = arr[i]
		for j:=i+1;j<n;j++{
			if arr[j]>rightMax{
				rightMax=arr[j]
			}
		}
		// Update the maximum water
		var minOfLMaxAndRMax int =leftMax
		if rightMax<minOfLMaxAndRMax{
			minOfLMaxAndRMax=rightMax
		}
		res = res+minOfLMaxAndRMax-arr[i]
	}
	return res
}

// Approach2: In the previous solution, to find the highest bar on the left and right,
//array traversal is needed which reduces the efficiency of the solution.
//To make this efficient one must pre-compute the highest bar on the left and right of every bar in linear
//time. Then use these pre-computed values to find the amount of water in every array.
func findWater1(arr []int, n int) int {
	// left[i] contains height of tallest bar to the
	// left of i'th bar including itself
	left := make([]int,n)

	// Right [i] contains height of tallest bar to
	// the right of ith bar including itself
	right := make([]int,n)

	// Initialize result
	var water int = 0

	// Fill left array
	left[0] = arr[0]
	for i:=1;i<n;i++{
		if left[i-1]>arr[i]{
			left[i]=left[i-1]
		} else{
			left[i]=arr[i]
		}
	}

	// Fill right array
	right[n - 1] = arr[n - 1]
	for i:=n-2;i>=0;i--{
		if right[i+1]>arr[i]{
			right[i]=right[i+1]
		} else {
			right[i]=arr[i]
		}
	}

	// Calculate the accumulated water element by element
	// consider the amount of water on i'th bar, the
	// amount of water accumulated on this particular
	// bar will be equal to min(left[i], right[i]) - arr[i] .
	for i:=0;i<n;i++{
		var minOfLMaxAndRMax int =left[i]
		if right[i]<minOfLMaxAndRMax{
			minOfLMaxAndRMax=right[i]
		}
		water = water+minOfLMaxAndRMax-arr[i]
	}
	return water
}

