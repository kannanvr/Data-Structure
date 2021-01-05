package Array
// find majority element in an array.
//Majority element is an element that appears more than n/2 times in an array of size n.

//-----------------naive approach time:O(n*n)------------------------
func findMajority(arr []int, n int) int{
	for _,v := range arr {
		count:=0
		for _, val := range arr {
			if val==v {
				count++
			}
		}
		if count>n/2 {
			return v
		}

	}
	return -1
}

//-----------------2-approach time:O(n), using moore vote counting algorithm------------------------
//this algorithm works in two part,
//1. find candidate for majority element if exist.
//2. count the occurrence of found candidate in step 1.


func findCandidate(arr []int) int {
	var majority, count int
	majority,count=0,1

	for i:=1;i<len(arr);i++{
		//if current is equal to majority then increment count else decrement count.
		if arr[majority]==arr[i]{
			count++
		} else {
			count--
		}
		//if count ==0 then change the majority to current element
		if count==0{
			majority=i
			count=1
		}
	}
	return arr[majority]
}

func majorityElement(nums []int) int {
	key := findCandidate(nums)
	var count int
	for _, v := range nums{
		if v==key{
			count++
		}
	}
	if count>len(nums)/2{
		return key
	}
	return -1
}