package Array
//www.geeksforgeeks.org/find-k-closest-elements-given-value/amp/
import (
	"fmt"
	"math"
)

//Q. Given a sorted array and an element x, find k closest elements to the x in an array.
//eg. ar=[12,15,18,21,22,43] k=4, x=20   O/p: 15,18,21,22

func k_closest_elements(arr []int,k,x int)  {
	most_closest := math.Abs(float64(arr[0]-x))
	most_closest_index:=0

	for i:=1;i<len(arr);i++{ //use binary search if array is sorted the time would be O(long+k) now it is O(n+k)
		if math.Abs(float64(arr[i]-x))<most_closest {
			most_closest =math.Abs(float64(arr[i]-x))
			most_closest_index=i
		}
	}
	l,r :=most_closest_index-1,most_closest_index+1
	if k>1{
		fmt.Println(most_closest)
		k--
		for l>=0 && r<len(arr) && k>0{
			if math.Abs(float64(arr[l]-x) < math.Abs(float64(arr[r]-x){

			}
		}
	}
}