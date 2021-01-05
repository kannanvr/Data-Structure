package Array

import (
	"math"
	"sort"
)

// finds the second largest element present in the array.
func secondMaxInArray(arr []int) int  {
	var firstLargest,secondLargest int = -1, -1
	for _, v := range arr {
		if v>firstLargest{
			secondLargest=firstLargest
			firstLargest=v
		}
		if v>secondLargest && v!=firstLargest{
			secondLargest=v
		}
	}
	return secondLargest
}


//Given a non-empty array of integers, return the third maximum number in this array.
//If it does not exist, return the maximum number. // https://leetcode.com/problems/third-maximum-number/
func thirdMax(nums []int) int {
	const min = math.MinInt32-1
	fl,sl,tl := min,min,min
	for _, v := range nums{
		if v>fl{
			tl=sl
			sl=fl
			fl=v
		} else if v>sl && v !=fl {
			tl=sl
			sl=v
		} else if v>tl && v !=sl && v!=fl {
			tl=v
		}

	}
	if tl== min{
		return fl
	}
	return tl
}




//if n is too high then above approach will not work efficiently
//Method 1 (Use Bubble k times), Time Complexity: O(nk)

func findKthLargestM1(nums []int, k int ) int  {
	for i:=0;i<k;i++{
		for j:=0;j<len(nums)-i-1;j++{
			if nums[j]>nums[j+1]{
				nums[j],nums[j+1] = nums[j+1],nums[j]
			}
		}
	}
	return nums[len(nums)-k]
}

//   Method 3(Use Sorting)
//1) Sort the elements in descending order in O(nLogn)
//2) Print the first k numbers of the sorted array O(k).
func findKthLargestM2(nums []int, k int ) int  {
	// https://tip.golang.org/src/sort/sort.go?s=4433:4458#L182
	sort.Ints(nums)
	return nums[len(nums)-k]
}


