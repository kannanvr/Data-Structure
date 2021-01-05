package main

func bubbleSort(nums []int) []int  {
	for i,_ := range nums{
		for j:=0;j<len(nums)-i-1;j++{
			if nums[j]>nums[j+1]{
				nums[j],nums[j+1] = nums[j+1],nums[j]
			}
		}
	}
	return nums
}


func optimizedBubbleSort(nums []int) []int  {
	for i,_ := range nums{
		swapped := false
		for j:=0;j<len(nums)-i-1;j++{
			if nums[j]>nums[j+1]{
				nums[j],nums[j+1] = nums[j+1],nums[j]
				swapped= true
			}
		}
		//if no two adjacent were swapped, ie it is in sorted now, hence break
		if !swapped{
			break
		}
	}
	return nums
}
