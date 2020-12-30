package Array



func twoSum(nums []int, target int) []int {
	numsMap:=make(map[int]int)
	for i, v:=range nums {
		required :=target-v
		if value, ok := numsMap[required];ok{
			return []int{i,value}
		} else {
			numsMap[v]=i
		}
	}
	return []int{}
}
