package Array

import (
	"math"
	"sort"
)

//approach 1: time: O(n*n*n)  space: O(1)
func maxProduct(arr []int, n int) int {
	// if size is less than 3, no triplet exists
	if n < 3 {
		return -1
	}

	// will contain max product
	maxProduct := math.MinInt32

	for i := 0; i < n - 2; i++{
		for j := i + 1; j < n - 1; j++{
			for k := j + 1; k < n; k++{
				product := arr[i]*arr[j]*arr[k]
				if maxProduct<product{
					maxProduct=product
				}
			}
		}

	}
	return maxProduct
}


//approach 2: time O(nlogn), space: O(1)
//Sort the array using some efficient in-place sorting algorithm in ascending order.
//Return the maximum of product of last three elements of the array and product of first two elements and last element.
func maximumProduct(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	max1 := nums[n-1]*nums[n-2]*nums[n-3]
	max2 := nums[0]*nums[1]*nums[n-1]
	if max1>max2 {
		return max1
	}
	return max2
}


//approach 3: time O(nlogn), space: O(1)
func maximumProduct1(nums []int) int {
	const min = math.MinInt32
	const max = math.MaxInt32

	//scan the array and find 3 maximum values in it
	fMax,sMax,tMax := min,min,min
	for _, v := range nums{
		if v>=fMax{
			tMax=sMax
			sMax=fMax
			fMax=v
		} else if v>=sMax && v !=fMax {
			tMax=sMax
			sMax=v
		} else if v>=tMax && v !=sMax && v!=fMax {
			tMax=v
		}

	}

	//scan the array and find 2 minimum values in it
	fMin,sMin := max,max
	for _, v := range nums{
		if v<=fMin{
			sMin=fMin
			fMin=v
		} else if v<=sMin && v !=fMin {
			sMin=v
		}
	}

	max1 := fMax*sMax*tMax
	max2 := fMin*sMin*fMax
	if max1>max2 {
		return max1
	}
	return max2

}

