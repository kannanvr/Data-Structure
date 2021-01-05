package Array

//remove all the occurrence of given val from array and return it's length.
// https://leetcode.com/problems/remove-element/  space O(1)
//idea is to transfer all the occurrence of val to last of array and ignore it.
//here order of elements are not guaranteed!!
func removeElement(nums []int, val int) int {
	var f int = len(nums)-1 //point to the last element of the array
	//traverse from last of the array
	for i:=len(nums)-1;i>=0;i-- {
		if nums[i]==val {
			nums[i],nums[f]=nums[f],nums[i] //swap current element with last non valued element
			f--
		}
	}
	//if there is only one element in array
	if f>0 && nums[f]==val{
		return f
	}
	return f+1

}

// shift all zeros to end keeping the order of remaining elements
func removeGivenElement(nums []int, val int) int {
	var f int = 0 //point to the last element of the array
	//traverse from last of the array
	for i:=0;i<len(nums);i++ {
		if nums[i]!=val {
			nums[i],nums[f]=nums[f],nums[i] //swap current element with last non valued element
			f++
		}
	}


}
//https://leetcode.com/problems/remove-duplicates-from-sorted-array/
//Given a sorted array nums, remove the duplicates in-place such that
//each element appears only once and returns the new length.  space O(1)

func removeDuplicates(nums []int) int {
	var f int
	for i,v := range nums {
		if nums[i] != nums[f] {
			f++
			nums[f]=v
		}
	}
	return f+1
}



 //Definition for singly-linked list.
 type ListNode struct {
      Val int
      Next *ListNode
 }
//delete duplicates from sorted singly list
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	current := head
	tmp     := current
	for current != nil {
		if current.Val != tmp.Val {
			tmp=tmp.Next
			tmp.Val=current.Val
		}

		current=current.Next
	}
	tmp.Next=nil
	return head

}