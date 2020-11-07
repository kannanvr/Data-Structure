package Array
//you have a sorted array of integers. write a function that return sorted array containing the squares of those integers.
//eg. ar=[-6,-4,1,2,3] o/p: [1,4,9,16,36]
func SortedArray(arr []int)  []int{
	//var ar1 []int create an array but not initialize memory, so it may throw panic error during runtime
	//var ar2 []int
	ar1 := make([]int,0)
	ar2 := make([]int,0)
	for _,value := range arr{
		if value<0{
			ar1 = append(ar1,value*value)
		} else {
			ar2 = append(ar2,value*value)
		}
	}
	i,j,k := 0,0,0 //k points to arr, i points to ar1 and j points to ar2
	for k<len(arr) {
		if ar1[i]<ar2[j]{
			arr[k]=ar1[i]
			i++
		} else {
			arr[k]=ar2[j]
			j++
		}
		k++
	}
	return arr
}
