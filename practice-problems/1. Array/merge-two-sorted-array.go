package Array

// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
//https://leetcode.com/problems/merge-sorted-array/
//here nums array having space to hold total of m+n elements
func merge(nums1 []int, m int, nums2 []int, n int)  {
	p1,p2 := m-1,n-1
	ri :=m+n-1
	for p1>=0 && p2>=0 {
		if nums1[p1]>nums2[p2]{
			nums1[ri]=nums1[p1]
			p1-=1
		} else{
			nums1[ri]=nums2[p2]
			p2-=1
		}
		ri-=1
	}

	for p2>=0{
		nums1[ri]=nums2[p2]
		p2-=1
		ri-=1
	}


}

// if you have to merge like array1 should be first part of sorted
// resultant array and arr2 should be 2nd part then use insertion sort.
/*
#User function Template for python3
def sortArray1(arr,n):
	key=arr[n]
	n,c=n-1,0
	while n>=0 and key<arr[n]:
		arr[n+1]=arr[n]
		c=1
		n-=1
	if c==1:
		arr[n+1]=key

def merge(arr1,arr2,n,m):
	#code here
	n,m=n-1,m-1
	while m>=0:
		if arr1[n]>arr2[m]:
			key=arr2[m]
			arr2[m]=arr1[n]
			arr1[n]=key
			sortArray1(arr1,n)
		m-=1
*/



//merge k sorted array: #https://medium.com/outco/how-to-merge-k-sorted-arrays-c35d87aa298e
