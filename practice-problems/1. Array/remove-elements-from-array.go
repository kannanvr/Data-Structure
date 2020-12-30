package Array

import "fmt"

//remove all the occurrence of given val from array and return it's length.
// https://leetcode.com/problems/remove-element/  space O(1)
//idea is to transfer all the occurrence of val to last of array and ignore it.

func removeElement(nums []int, val int) int {
	var f int = len(nums)-1
	var c int

	for i:=len(nums)-1;i>=0;i-- {
		if nums[i]==val {
			nums[i],nums[f]=nums[f],nums[i]
			f--
			c++
		}
	}
	fmt.Println(nums,f)
	return len(nums)-c

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